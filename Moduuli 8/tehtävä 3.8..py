import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Eemeli04',
    autocommit=True,
    collation='utf8mb4_general_ci')

from geopy import distance

def fetch_airport_by_icao_1(code):
    icao_1 = f"select latitude_deg, longitude_deg from airport where ident ='{code}';"
    cursor = connection.cursor()
    cursor.execute(icao_1)
    result_row = cursor.fetchone()
    # print(result_row)
    return result_row
def fetch_airport_by_icao_2(code):
    icao_2 = f"select latitude_deg, longitude_deg from airport where ident ='{code}';"
    cursor = connection.cursor()
    cursor.execute(icao_2)
    result_row = cursor.fetchone()
    # print(result_row)
    return result_row
user_input_1 = input("Anna ICAO-koodi")
user_input_2 = input("Anna ICAO-koodi")
result_1= fetch_airport_by_icao_1(user_input_1)
result_2= fetch_airport_by_icao_2(user_input_2)
result_distance = distance.distance(result_1, result_2).km
print(f"{result_distance:.2f} kilometriä")


