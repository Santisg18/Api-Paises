from flask import Flask, jsonify
from flask_cors import CORS
import requests
 
app = Flask(__name__)
CORS(app)
 
@app.route("/continentes/")
def obtener_continentes():
     r = requests.get("https://restcountries.eu/rest/v2/all")
     listap = r.json()
     continentes = set()
     for i in range(0,len(listap)):
         continentes.add(listap[i]["region"])
    
     return jsonify(list(sorted(continentes)))


@app.route('/listapaises/<string:continente>')
def consultar_paises(continente):
    r = requests.get("https://restcountries.eu/rest/v2/region/" + continente)
    print("El error es " + str(r.status_code))
    if(r.status_code == 200):
        print(type(r.json()))
        return jsonify(r.json())
    else:
        return"Culpa del COVID-19"


@app.route('/listafronteras/<string:pais>')
def consultar_fronteras(pais):
    r = requests.get("https://restcountries.eu/rest/v2/name/" + pais)
    print("El error es " + str(r.status_code))
    if(r.status_code == 200):
        print(type(r.json()))
        return jsonify(r.json())
    else:
        return"Culpa del COVID-19"


@app.route('/listaInfo/<string:paises>')
def consultar_info(paises):
    r = requests.get("https://restcountries.eu/rest/v2/name/" + paises)
    print("El error es " + str(r.status_code))
    if(r.status_code == 200):
        print(type(r.json()))
        return jsonify(r.json())
    else:
        return"Culpa del COVID-19"


@app.route('/listaInfo2/<string:paises2>')
def consultar_info2(paises2):
    r = requests.get("https://restcountries.eu/rest/v2/alpha?codes=" + paises2)
    print("El error es " + str(r.status_code))
    if(r.status_code == 200):
        print(type(r.json()))
        return jsonify(r.json())
    else:
        return"Culpa del COVID-19"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2501)

