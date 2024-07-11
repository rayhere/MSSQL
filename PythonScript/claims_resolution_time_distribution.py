import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_resolution_time = '''
    SELECT DATEDIFF(day, C.ClaimDate, C.ResolutionDate) AS ResolutionTimeDays
    FROM Claims C
    WHERE C.ResolutionDate IS NOT NULL
    '''

    df_resolution_time = pd.read_sql(query_resolution_time, conn)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.hist(df_resolution_time['ResolutionTimeDays'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Resolution Time (Days)')
    plt.ylabel('Number of Claims')
    plt.title('Distribution of Claims Resolution Time')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
