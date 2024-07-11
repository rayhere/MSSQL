import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    # Query to retrieve latest compliance status for each employer
    query_latest_compliance = '''
    SELECT E.EmployerName, CI.ComplianceType, CI.ComplianceStatus, CI.ComplianceDate
    FROM (
        SELECT EmployerID, MAX(ComplianceDate) AS MaxComplianceDate
        FROM ComplianceInfo
        GROUP BY EmployerID
    ) AS LatestCompliance
    JOIN ComplianceInfo CI ON LatestCompliance.EmployerID = CI.EmployerID AND LatestCompliance.MaxComplianceDate = CI.ComplianceDate
    JOIN Employers E ON CI.EmployerID = E.EmployerID
    '''

    # Execute the query and fetch results into a DataFrame
    df_latest_compliance = pd.read_sql(query_latest_compliance, conn)

    # Display the result
    print(df_latest_compliance)
    
    # Data Analysis and Visualization
    # Count of compliance statuses
    compliance_counts = df_latest_compliance['ComplianceStatus'].value_counts()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.countplot(x='ComplianceStatus', data=df_latest_compliance, palette='Set2')
    plt.title('Latest Compliance Status by Employer')
    plt.xlabel('Compliance Status')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server or executing query: {e}")
