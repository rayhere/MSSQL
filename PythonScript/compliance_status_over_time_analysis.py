import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_compliance_over_time = '''
    SELECT ComplianceDate, ComplianceStatus, COUNT(*) AS NumOccurrences
    FROM ComplianceInfo
    GROUP BY ComplianceDate, ComplianceStatus
    ORDER BY ComplianceDate
    '''

    df_compliance_over_time = pd.read_sql(query_compliance_over_time, conn)

    # Pivot table for better visualization
    df_pivot_compliance = df_compliance_over_time.pivot(index='ComplianceDate', columns='ComplianceStatus', values='NumOccurrences').fillna(0)

    # Plotting
    plt.figure(figsize=(12, 8))
    df_pivot_compliance.plot(kind='area', stacked=True)
    plt.xlabel('Compliance Date')
    plt.ylabel('Number of Occurrences')
    plt.title('Compliance Status Over Time')
    plt.legend(title='Compliance Status')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
