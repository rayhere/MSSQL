import pyodbc
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to SQL Server successfully!")

    # Example of deleting inactive employers and related data
    delete_query = '''
    DELETE FROM Employees
    WHERE EmployerID IN (
        SELECT EmployerID
        FROM Employers
        WHERE IsActive = 0
    );

    DELETE FROM CoverageDetails
    WHERE EmployerID IN (
        SELECT EmployerID
        FROM Employers
        WHERE IsActive = 0
    );

    DELETE FROM Claims
    WHERE EmployerID IN (
        SELECT EmployerID
        FROM Employers
        WHERE IsActive = 0
    );

    DELETE FROM ComplianceInfo
    WHERE EmployerID IN (
        SELECT EmployerID
        FROM Employers
        WHERE IsActive = 0
    );

    DELETE FROM Employers
    WHERE IsActive = 0;
    '''

    # Execute the delete operations
    cursor = conn.cursor()
    cursor.execute(delete_query)
    conn.commit()

    print("Inactive employers and their related data deleted successfully.")
    
    # After deletion, perform data analysis and visualization
    # Query remaining employers by city
    query_employers_by_city = '''
    SELECT City, COUNT(*) AS NumEmployers
    FROM Employers
    GROUP BY City
    ORDER BY NumEmployers DESC
    '''

    # Fetch results into a DataFrame
    df_employers_by_city = pd.read_sql(query_employers_by_city, conn)

    # Display the result
    print("\nEmployers remaining after deletion:")
    print(df_employers_by_city)

    # Plotting
    plt.figure(figsize=(10, 6))
    sns.barplot(x='NumEmployers', y='City', data=df_employers_by_city, palette='coolwarm')
    plt.xlabel('Number of Employers')
    plt.ylabel('City')
    plt.title('Number of Employers Remaining by City')
    plt.tight_layout()
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server or executing query: {e}")
