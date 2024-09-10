import mysql.connector

connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Eemeli04',
         autocommit=True,
         collation ='utf8mb4_general_ci')