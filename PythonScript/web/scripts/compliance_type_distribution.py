from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve claim description data
def fetch_claim_description_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to retrieve claim descriptions
        query_claim_description = '''
        SELECT ClaimDescription, COUNT(*) AS NumClaims
        FROM Claims
        GROUP BY ClaimDescription
        ORDER BY NumClaims DESC
        '''

        # Fetch data into a DataFrame
        df_claim_description = pd.read_sql(query_claim_description, conn)

        return df_claim_description

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/claims_description_distribution', methods=['GET'])
def claims_description_distribution():
    # Fetch claim description data
    df_claim_description = fetch_claim_description_data()

    if df_claim_description is None:
        return render_template('error.html', message='Failed to fetch claim description data.')

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.pie(df_claim_description['NumClaims'], labels=df_claim_description['ClaimDescription'], autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title('Distribution of Claims by Description')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/claims_description_distribution_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('claims_description_distribution.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
