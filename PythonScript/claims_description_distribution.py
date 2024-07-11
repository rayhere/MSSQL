import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_claim_description = '''
    SELECT ClaimDescription, COUNT(*) AS NumClaims
    FROM Claims
    GROUP BY ClaimDescription
    ORDER BY NumClaims DESC
    '''

    df_claim_description = pd.read_sql(query_claim_description, conn)

    # Plotting
    plt.figure(figsize=(12, 8))
    plt.bar(df_claim_description['ClaimDescription'][:10], df_claim_description['NumClaims'][:10], color='skyblue')
    plt.xlabel('Claim Description')
    plt.ylabel('Number of Claims')
    plt.title('Claims Distribution by Claim Description')
    plt.xticks(rotation=45)
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
