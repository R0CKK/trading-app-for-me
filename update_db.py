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

# Create a cursor object (dictionary format)
cursor = connection.cursor(dictionary=True)

# Retrieve existing symbols (same as before)
cursor.execute("""SELECT symbol FROM stock""")
rows = cursor.fetchall()
existing_symbols = {row['symbol'] for row in rows}  # Set comprehension for efficient lookup

# Alpaca API connection (same as before)
api = tradeapi.REST('PKZCZF36WHC5VG8P7PLH','6i03dgYCPoZxlgRSThr7Gxi8JAdyVwAbKRxlCunk',base_url='https://paper-api.alpaca.markets')

# Fetch tradable assets (same as before)
assets = api.list_assets()

# Check for new tradable assets (modified logic)
for asset in assets:
  if asset.tradable and asset.symbol not in existing_symbols:
    # Prepare SQL statement with placeholders
    sql = "INSERT INTO stock (symbol, company) VALUES (%s, %s)"
    # Create a tuple with data for the prepared statement
    data = (asset.symbol, asset.name)
    # Execute the prepared statement with data
    cursor.execute(sql, data)
    print(asset)

# Commit changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
