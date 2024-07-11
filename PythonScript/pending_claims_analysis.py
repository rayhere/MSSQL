import pandas as pd
import pyodbc
import seaborn as sns
import matplotlib.pyplot as plt

# Establish a connection to the NYSIFDB database
conn_str = 'DRIVER={SQL Server};SERVER=RAYMOND-PC\\SQL1;DATABASE=NYSIFDB;Trusted_Connection=yes;'
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
    
    # Display the result
    print(df_pending_claims)
    
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
    plt.show()

except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
