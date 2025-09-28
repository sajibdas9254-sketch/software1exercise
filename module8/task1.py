import sqlite3


conn = sqlite3.connect("airports.db")
cursor = conn.cursor()

icao = input("Enter ICAO code: ").upper()


cursor.execute("SELECT name, municipality FROM airport WHERE ident = ?", (icao,))
result = cursor.fetchone()

if result:
    print(f"Airport name: {result[0]}")
    print(f"Location (town): {result[1]}")
else:
    print("No airport found with that ICAO code.")

conn.close()