import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Eemeli04',
    autocommit=True,
    collation='utf8mb4_general_ci')

def  describe_airport(maakoodi):
    sql = f"select type, count(*) from airport where iso_country = '{maakoodi}' group by type;"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    return result_row

user_input = input("Anna lentokentän maakoodi: ")
result = describe_airport(user_input)
if result:
    print(f"Haettu kenttä: {result}")
else:
    print("Kenttää ei löydy")


