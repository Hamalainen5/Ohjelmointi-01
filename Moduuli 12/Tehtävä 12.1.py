import requests
response = requests.get('https://api.chucknorris.io/jokes/random')
# parsitaan response body json formaatista
# pythonin vastaava tietorakenne
response_body = response.json()
# tulostetaan ensimmäinen hakutulos
for value in response_body['value']:
    print(value, end="")
