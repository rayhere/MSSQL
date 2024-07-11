import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_employee_age = '''
    SELECT DATEDIFF(YEAR, DateOfBirth, GETDATE()) AS Age
    FROM Employees
    '''

    df_employee_age = pd.read_sql(query_employee_age, conn)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.hist(df_employee_age['Age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Age')
    plt.ylabel('Number of Employees')
    plt.title('Employee Age Distribution')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
