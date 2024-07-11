import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_coverage_amounts = '''
    SELECT CoverageAmount
    FROM CoverageDetails
    '''

    df_coverage_amounts = pd.read_sql(query_coverage_amounts, conn)

    # Plotting
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df_coverage_amounts['CoverageAmount'], orient='v', color='lightblue')
    plt.ylabel('Coverage Amount')
    plt.title('Distribution of Coverage Amounts')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
