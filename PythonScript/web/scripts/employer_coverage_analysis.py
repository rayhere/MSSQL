import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

@app.route('/employer_coverage_analysis')
def employer_coverage_analysis():
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

        df_coverage = pd.read_sql(query_coverage, conn)

        # Plotting
        plt.figure(figsize=(10, 6))
        sns.barplot(x='EmployerName', y='TotalCoverageAmount', data=df_coverage, palette='coolwarm')
        plt.xlabel('Employer Name')
        plt.ylabel('Total Coverage Amount')
        plt.title('Total Coverage Amount by Employer')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a file (optional)
        plot_file = 'static/employer_coverage_analysis.png'  # adjust path as needed
        plt.savefig(plot_file)

        return render_template('employer_coverage_analysis.html', plot_file=plot_file)

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return render_template('error.html', message='Error connecting to SQL Server')

if __name__ == '__main__':
    app.run(debug=True)
