from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve employee age data
def fetch_employee_age_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to retrieve employee ages
        query_employee_age = '''
        SELECT DATEDIFF(YEAR, DateOfBirth, GETDATE()) AS Age
        FROM Employees
        '''

        # Fetch data into a DataFrame
        df_employee_age = pd.read_sql(query_employee_age, conn)

        return df_employee_age

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/employee_age_distribution', methods=['GET'])
def employee_age_distribution():
    # Fetch employee age data
    df_employee_age = fetch_employee_age_data()

    if df_employee_age is None:
        return render_template('error.html', message='Failed to fetch employee age data.')

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.hist(df_employee_age['Age'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        plt.xlabel('Age')
        plt.ylabel('Number of Employees')
        plt.title('Employee Age Distribution')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/employee_age_distribution_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('employee_age_distribution.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
