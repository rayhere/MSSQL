from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve compliance type data
def fetch_compliance_type_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to retrieve compliance types
        query_compliance_type = '''
        SELECT ComplianceType, COUNT(*) AS NumOccurrences
        FROM ComplianceInfo
        GROUP BY ComplianceType
        ORDER BY NumOccurrences DESC
        '''

        # Fetch data into a DataFrame
        df_compliance_type = pd.read_sql(query_compliance_type, conn)

        return df_compliance_type

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/compliance_type_distribution', methods=['GET'])
def compliance_type_distribution():
    # Fetch compliance type data
    df_compliance_type = fetch_compliance_type_data()

    if df_compliance_type is None:
        return render_template('error.html', message='Failed to fetch compliance type data.')

    try:
        # Plotting
        plt.figure(figsize=(12, 8))
        plt.bar(df_compliance_type['ComplianceType'][:10], df_compliance_type['NumOccurrences'][:10], color='skyblue')
        plt.xlabel('Compliance Type')
        plt.ylabel('Number of Occurrences')
        plt.title('Distribution of Compliance Types')
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/compliance_type_distribution_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('compliance_type_distribution.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
