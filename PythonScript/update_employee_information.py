import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")
    
    # Example of updating employee information
    update_query = '''
    UPDATE Employees
    SET Department = 'New Department'
    WHERE EmployeeID = 1
    '''

    # Execute the update query
    cursor = conn.cursor()
    cursor.execute(update_query)
    conn.commit()

    print("Employee information updated successfully.")
    
    # Data Analysis and Visualization Example (after update)
    # Query to retrieve updated employee information
    query_updated_employee = '''
    SELECT FirstName, LastName, Department
    FROM Employees
    WHERE EmployeeID = 1
    '''
    
    # Fetch results into a DataFrame
    df_updated_employee = pd.read_sql(query_updated_employee, conn)
    
    # Display the updated employee information
    print("Updated Employee Information:")
    print(df_updated_employee)
    
    # Data Visualization (example)
    # Count of employees by department
    query_employees_by_department = '''
    SELECT Department, COUNT(*) AS NumEmployees
    FROM Employees
    GROUP BY Department
    '''
    
    df_employees_by_department = pd.read_sql(query_employees_by_department, conn)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NumEmployees', y='Department', data=df_employees_by_department, palette='coolwarm')
    plt.xlabel('Number of Employees')
    plt.ylabel('Department')
    plt.title('Number of Employees by Department')
    plt.tight_layout()
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server or executing query: {e}")
