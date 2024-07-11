import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    query_employees = '''
    SELECT E.EmployerName, COUNT(*) AS NumEmployees
    FROM Employers E
    JOIN Employees Emp ON E.EmployerID = Emp.EmployerID
    GROUP BY E.EmployerName
    '''

    df_employees = pd.read_sql(query_employees, conn)

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NumEmployees', y='EmployerName', data=df_employees, palette='coolwarm')
    plt.xlabel('Number of Employees')
    plt.ylabel('Employer Name')
    plt.title('Employee Count by Employer')
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
