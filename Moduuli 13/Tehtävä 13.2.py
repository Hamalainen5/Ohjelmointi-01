import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Eemeli04',
         autocommit=True,
         collation ='utf8mb4_general_ci')
# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
app = Flask(__name__)
@app.route('/Kenttä/<code>')
def kenttä(code):
    sql = f"select name, municipality from airport where ident ='{code}';"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    # print(result_row)
    vastaus = {
        "ICAO:": code, "Name:": result_row[0], "Municipality:": result_row[1]
        }
    return vastaus
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
