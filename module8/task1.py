import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'flightgame',
    password = 'flightgame',
    database='airport',
    autocommit = True
)


ICAO_code = input("Enter the ICAO code of an airport: ")
SQL = f"Select name, municipality FROM airport WHERE ident = '{ICAO_code}'"
SQL_cursor = connection.cursor()
SQL_cursor.execute(SQL)
result = SQL_cursor.fetchone()
print (f"Airport name: {result[0]}\nLocation: {result[1]}")