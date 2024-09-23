import mysql.connector
import alpaca_trade_api as tradeapi

# Replace with your MySQL connection details
connection_details = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_database'
}

connection = mysql.connector.connect(**connection_details)

cursor = connection.cursor()

api = tradeapi.REST('PKZCZF36WHC5VG8P7PLH','6i03dgYCPoZxlgRSThr7Gxi8JAdyVwAbKRxlCunk',base_url='https://paper-api.alpaca.markets')

assets = api.list_assets()

for asset in assets:
  if asset.tradable:
    sql = "INSERT INTO stock (symbol, company) VALUES (%s, %s)"
    data = (asset.symbol, asset.name)
    cursor.execute(sql, data)


connection.commit()

cursor.close()
connection.close()
