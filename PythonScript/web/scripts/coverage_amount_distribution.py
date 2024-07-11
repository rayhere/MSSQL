from flask import Flask, render_template
import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve compliance status data over time
def fetch_compliance_status_over_time():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to retrieve compliance status over time
        query_compliance_over_time = '''
        SELECT ComplianceDate, ComplianceStatus, COUNT(*) AS NumOccurrences
        FROM ComplianceInfo
        GROUP BY ComplianceDate, ComplianceStatus
        ORDER BY ComplianceDate
        '''

        # Fetch data into a DataFrame
        df_compliance_over_time = pd.read_sql(query_compliance_over_time, conn)

        return df_compliance_over_time

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/compliance_status_over_time', methods=['GET'])
def compliance_status_over_time():
    # Fetch compliance status over time data
    df_compliance_over_time = fetch_compliance_status_over_time()

    if df_compliance_over_time is None:
        return render_template('error.html', message='Failed to fetch compliance status over time data.')

    try:
        # Pivot table for better visualization
        df_pivot_compliance = df_compliance_over_time.pivot(index='ComplianceDate', columns='ComplianceStatus', values='NumOccurrences').fillna(0)

        # Plotting
        plt.figure(figsize=(12, 8))
        df_pivot_compliance.plot(kind='area', stacked=True)
        plt.xlabel('Compliance Date')
        plt.ylabel('Number of Occurrences')
        plt.title('Compliance Status Over Time')
        plt.legend(title='Compliance Status')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/compliance_status_over_time_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('compliance_status_over_time.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
