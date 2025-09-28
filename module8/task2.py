import sqlite3


conn = sqlite3.connect("airports.db")
cursor = conn.cursor()


country = input("Enter area code (e.g. FI): ").upper()

cursor.execute("""
    SELECT type, COUNT(*) 
    FROM airport 
    WHERE iso_country = ? 
    GROUP BY type 
    ORDER BY type
""", (country,))


if results:
    print(f"\nAirports in {country}:")
    for row in results:
        print(f"{row[1]} {row[0]}")
else:
    print("No airports found for that country code.")


conn.close()