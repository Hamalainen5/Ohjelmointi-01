import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Eemeli04',
         autocommit=True,
         collation ='utf8mb4_general_ci')
cursor = connection.cursor()
cursor.execute("SELECT name, iso_country from country")
#result = cursor.fetchone()
#print(result[0])
#result = cursor.fetchmany(3)
#print(result)
result = cursor.fetchall()
print(result)

print(cursor.rowcount)
print(result)
print(result[1][1])
for row in result:
    print(f"maan {row[0]} maakoodi on {row[1]}.")
print(f"maita yhteensä: {cursor.rowcount}")
if cursor.rowcount == 0:
    print("ei yhtään maata.")