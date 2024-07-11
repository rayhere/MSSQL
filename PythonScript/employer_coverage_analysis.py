import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")
    
    # Query to calculate total coverage amount by employer
    query_coverage = '''
    SELECT E.EmployerName, SUM(CD.CoverageAmount) AS TotalCoverageAmount
    FROM Employers E
    JOIN CoverageDetails CD ON E.EmployerID = CD.EmployerID
    GROUP BY E.EmployerName
    '''

    # Execute the query and fetch results into a DataFrame
    df_coverage = pd.read_sql(query_coverage, conn)

    # Visualize total coverage amount by employer
    plt.figure(figsize=(10, 6))
    plt.bar(df_coverage['EmployerName'], df_coverage['TotalCoverageAmount'])
    plt.xlabel('Employer Name')
    plt.ylabel('Total Coverage Amount')
    plt.title('Total Coverage Amount by Employer')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
