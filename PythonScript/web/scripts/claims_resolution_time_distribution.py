from flask import Flask, render_template
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Function to retrieve data and preprocess it
def fetch_resolution_time_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Query to fetch resolution time for claims
        query_resolution_time = '''
        SELECT DATEDIFF(day, C.ClaimDate, C.ResolutionDate) AS ResolutionTimeDays
        FROM Claims C
        WHERE C.ResolutionDate IS NOT NULL
        '''

        # Fetch data into a DataFrame
        df_resolution_time = pd.read_sql(query_resolution_time, conn)

        return df_resolution_time

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None

@app.route('/claims_resolution_time', methods=['GET'])
def claims_resolution_time():
    # Fetch claims resolution time data
    df_resolution_time = fetch_resolution_time_data()

    if df_resolution_time is None:
        return render_template('error.html', message='Failed to fetch claims resolution time data.')

    try:
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.hist(df_resolution_time['ResolutionTimeDays'], bins=20, color='skyblue', edgecolor='black', alpha=0.7)
        plt.xlabel('Resolution Time (Days)')
        plt.ylabel('Number of Claims')
        plt.title('Distribution of Claims Resolution Time')
        plt.tight_layout()

        # Save the plot to a temporary file
        plot_file = 'static/claims_resolution_time_plot.png'  # Assuming 'static' folder exists
        plt.savefig(plot_file)
        plt.close()

        # Encode the plot image to base64
        with open(plot_file, 'rb') as f:
            plot_data = f.read()
        plot_base64 = base64.b64encode(plot_data).decode('utf-8')

        # Render the HTML template with the plot image
        return render_template('claims_resolution_time.html', plot_url=plot_base64)

    except Exception as e:
        print(f"Error during plotting: {e}")
        return render_template('error.html', message='Error during plotting.')

if __name__ == '__main__':
    app.run(debug=True)
