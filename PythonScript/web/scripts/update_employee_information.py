import pyodbc
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

@app.route('/update_employee_information', methods=['GET', 'POST'])
def update_employee_information():
    if request.method == 'POST':
        try:
            conn = pyodbc.connect(conn_str)
            print("Connected to SQL Server successfully!")

            # Example of updating employee information
            employee_id = request.form['employee_id']
            new_department = request.form['new_department']

            update_query = f'''
            UPDATE Employees
            SET Department = '{new_department}'
            WHERE EmployeeID = {employee_id}
            '''

            # Execute the update query
            cursor = conn.cursor()
            cursor.execute(update_query)
            conn.commit()

            print("Employee information updated successfully.")

            # Data Analysis and Visualization Example (after update)
            # Query to retrieve updated employee information
            query_updated_employee = f'''
            SELECT FirstName, LastName, Department
            FROM Employees
            WHERE EmployeeID = {employee_id}
            '''

            # Fetch results into a DataFrame
            df_updated_employee = pd.read_sql(query_updated_employee, conn)

            # Plotting (example: count of employees by department)
            query_employees_by_department = '''
            SELECT Department, COUNT(*) AS NumEmployees
            FROM Employees
            GROUP BY Department
            '''

            df_employees_by_department = pd.read_sql(query_employees_by_department, conn)

            # Render template with updated employee information and visualization
            return render_template('update_employee_information.html',
                                   employee_info=df_updated_employee.to_html(index=False),
                                   department_counts=df_employees_by_department.to_html(index=False))

        except pyodbc.Error as e:
            print(f"Error connecting to SQL Server or executing query: {e}")
            return render_template('error.html', message='Error connecting to SQL Server or executing query')

    return render_template('update_employee_form.html')

if __name__ == '__main__':
    app.run(debug=True)
