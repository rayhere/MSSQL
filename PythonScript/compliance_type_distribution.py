import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_compliance_type = '''
    SELECT CI.ComplianceType, COUNT(*) AS NumOccurrences
    FROM ComplianceInfo CI
    GROUP BY CI.ComplianceType
    ORDER BY NumOccurrences DESC
    '''

    df_compliance_type = pd.read_sql(query_compliance_type, conn)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.pie(df_compliance_type['NumOccurrences'], labels=df_compliance_type['ComplianceType'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Distribution of Compliance Types')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
