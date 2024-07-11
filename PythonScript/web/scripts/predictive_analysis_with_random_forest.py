from flask import Flask, render_template, request
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pyodbc

app = Flask(__name__)

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'

# Example function to retrieve and preprocess data (X, y)
def load_data():
    try:
        conn = pyodbc.connect(conn_str)
        print("Connected to SQL Server successfully!")

        # Example query to retrieve data for predictive analysis
        query_data = '''
        SELECT feature1, feature2, ..., featureN, label
        FROM YourDataTable
        '''

        # Fetch data into a DataFrame
        df = pd.read_sql(query_data, conn)

        # Split data into features (X) and labels (y)
        X = df.drop('label', axis=1)  # Adjust based on your actual data structure
        y = df['label']

        return X, y

    except pyodbc.Error as e:
        print(f"Error connecting to SQL Server or executing query: {e}")
        return None, None

@app.route('/predictive_analysis', methods=['GET', 'POST'])
def predictive_analysis():
    if request.method == 'POST':
        try:
            # Load data for predictive analysis
            X, y = load_data()

            if X is None or y is None:
                return render_template('error.html', message='Failed to load data for predictive analysis')

            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train a Random Forest classifier
            model = RandomForestClassifier()
            model.fit(X_train, y_train)

            # Make predictions on the test set
            predictions = model.predict(X_test)

            # Calculate accuracy of the model
            accuracy = accuracy_score(y_test, predictions)

            return render_template('predictive_analysis_result.html', accuracy=accuracy)

        except Exception as e:
            print(f"Error during predictive analysis: {e}")
            return render_template('error.html', message='Error during predictive analysis')

    return render_template('predictive_analysis_form.html')

if __name__ == '__main__':
    app.run(debug=True)
