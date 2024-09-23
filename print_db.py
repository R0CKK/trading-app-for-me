import mysql.connector
import alpaca_trade_api as tradeapi

# Replace with your MySQL connection details
connection_details = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

# Connect to the database
connection = mysql.connector.connect(**connection_details)

# Create a cursor object
cursor = connection.cursor(dictionary=True)

# Retrieve data (same as before)
cursor.execute("""SELECT symbol,company FROM stock""")
rows = cursor.fetchall()

# Print symbols (same as before)
for row in rows:
    print(row['symbol'])

# Close the cursor and connection
cursor.close()
connection.close()
