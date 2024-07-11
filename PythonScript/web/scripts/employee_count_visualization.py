from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve data and preprocess it
def fetch_employee_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to fetch employee counts by employer
        query_employees = '''
        SELECT E.EmployerName, COUNT(*) AS NumEmployees
        FROM Employers E
        JOIN Employees Emp ON E.EmployerID = Emp.EmployerID
        GROUP BY E.EmployerName
        '''

        # Fetch data into a DataFrame
        df_employees = pd.read_sql(query_employees, conn)

        return df_employees

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/employee_count', methods=['GET'])
def employee_count():
    # Fetch employee data
    df_employees = fetch_employee_data()

    if df_employees is None:
        return render_template('error.html', message='Failed to fetch employee data.')

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        sns.barplot(x='NumEmployees', y='EmployerName', data=df_employees, palette='coolwarm')
        plt.xlabel('Number of Employees')
        plt.ylabel('Employer Name')
        plt.title('Employee Count by Employer')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/employee_count_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Render the HTML template with the plot image
        return render_template('employee_count.html', plot_url=plot_file)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
