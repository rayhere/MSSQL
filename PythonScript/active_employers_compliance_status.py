import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")
    
    # Query to retrieve active employers and their compliance status
    query_active_employers = '''
    SELECT E.EmployerName, CI.ComplianceType, CI.ComplianceStatus, CI.ComplianceDate
    FROM Employers E
    JOIN ComplianceInfo CI ON E.EmployerID = CI.EmployerID
    WHERE E.IsActive = 1
    '''
    
    # Execute the query and fetch results into a DataFrame
    df_active_employers = pd.read_sql(query_active_employers, conn)
    
    # Display the result
    print(df_active_employers)
    
    # Data Analysis and Visualization
    # Count of compliance statuses
    compliance_counts = df_active_employers['ComplianceStatus'].value_counts()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.countplot(x='ComplianceStatus', data=df_active_employers, palette='Set2')
    plt.title('Compliance Status of Active Employers')
    plt.xlabel('Compliance Status')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
