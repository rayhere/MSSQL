import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt
from flask import Flask, render_template

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

@app.route('/pending_claims_analysis')
def pending_claims_analysis():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to find employees with pending claims
        query_pending_claims = '''
        SELECT E.FirstName, E.LastName, C.ClaimDate, C.ClaimDescription, C.ClaimStatus
        FROM Employees E
        JOIN Claims C ON E.EmployeeID = C.EmployeeID
        WHERE C.ClaimStatus = 'Pending'
        '''

        # Execute the query and fetch results into a DataFrame
        df_pending_claims = pd.read_sql(query_pending_claims, conn)

        # Data Analysis and Visualization
        # Count of pending claims by employee
        pending_claims_count = df_pending_claims.groupby(['FirstName', 'LastName'])['ClaimStatus'].count().reset_index()
        pending_claims_count = pending_claims_count.rename(columns={'ClaimStatus': 'NumPendingClaims'})

        # Plotting
        plt.figure(figsize=(12, 6))
        sns.barplot(x='NumPendingClaims', y='LastName', data=pending_claims_count, palette='viridis')
        plt.xlabel('Number of Pending Claims')
        plt.ylabel('Employee Last Name')
        plt.title('Number of Pending Claims by Employee')
        plt.tight_layout()

        # Save the plot to a file (optional)
        plot_file = 'static/pending_claims_analysis.png'  # adjust path as needed
        plt.savefig(plot_file)

        return render_template('pending_claims_analysis.html', plot_file=plot_file)

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server: {e}")
        return render_template('error.html', message='Error connecting to SQL Server')

if __name__ == '__main__':
    app.run(debug=True)
