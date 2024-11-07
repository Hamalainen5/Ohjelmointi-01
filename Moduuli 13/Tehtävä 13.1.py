#Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    args = request.args
    number = int(args['number'])
    isPrime = True
    for jakaja in range(2, number):
        if number % jakaja == 0:
            isPrime = False
            break
    if isPrime:
        vastaus = {
            "number": number,
            "isPrime": isPrime
        }
        return vastaus

    else:
        vastaus = {
            "number": number,
            "isPrime": isPrime
        }
        return vastaus



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

# haku tulee kirjoittaa esim. seuraavassa muodossa
# http://127.0.0.1:3000/alkuluku?number=31
# En osannut tehdä tehtävästä sellaista, että pelkän numeron kirjoittaminen riittää
