from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve coverage amount data
def fetch_coverage_amount_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to retrieve coverage amounts
        query_coverage_amounts = '''
        SELECT CoverageAmount
        FROM CoverageDetails
        '''

        # Fetch data into a DataFrame
        df_coverage_amounts = pd.read_sql(query_coverage_amounts, conn)

        return df_coverage_amounts

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/coverage_amount_distribution', methods=['GET'])
def coverage_amount_distribution():
    # Fetch coverage amount data
    df_coverage_amounts = fetch_coverage_amount_data()

    if df_coverage_amounts is None:
        return render_template('error.html', message='Failed to fetch coverage amount data.')

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df_coverage_amounts['CoverageAmount'], orient='v', color='lightblue')
        plt.ylabel('Coverage Amount')
        plt.title('Distribution of Coverage Amounts')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/coverage_amount_distribution_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('coverage_amount_distribution.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
