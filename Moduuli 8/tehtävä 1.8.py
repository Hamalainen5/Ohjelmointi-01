import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Eemeli04',
         autocommit=True,
         collation ='utf8mb4_general_ci')

#funktio joka pystyy hakemaan lentoaseman ICAO-koodin perusteella
def fetch_airport_by_icao(code):
    sql = f"select name, municipality from airport where ident ='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    #print(result_row)
    return result_row

user_input = input("Anna ICAO-koodi: ")
result = fetch_airport_by_icao(user_input)
if result:
    print(f"Haettu kenttä: {result[0]},{result[1]}")
else:
    print("Kenttää ei löydy")
