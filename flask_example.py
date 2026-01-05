############################
## Flask
## build end-to-end web application
## 1. Web server gateway interface (WSGI: Webszerver-WebApp felépítés)
## 2. Jinja 2: Template engine, dynamic webpages (WebTemplate+DataSource(db, ml modul, stb))
############################
##

"""
Flask: API végpont

Lekérdezés: 
curl -X POST "http://127.0.0.1:5001/query" \
     -H "Content-Type: application/json" \
     -d '{"name":"Tom","age":"32"}'
"""

from flask import Flask, request, jsonify, render_template
app = Flask(__name__) # inicializálás

## Főoldal, egyszerű static válasz
@app.route('/', methods=['get'])
def welcome():
    return ("Welcome!")


# Felhasználói kérdés indítása, "form" minta, ami külön HTML fájlban definiált
@app.route('/hello', methods=['post','get'])
def handle_hello_get():
    return render_template('index.html') #Jinja2 template engine

# Felhasználói kérdés feldolgozása, form feldolozása mutata ide
@app.route('/submit', methods=['post','get'])
def submit():
    if request.method=="POST":
        name=request.form['name']
        return f'Hello {name}'
    return render_template('index.html') #Jinja2 template engine
    #return redirect(url_for()) ## vagy átirányítás

# Felhasználói kérdés feldolgozása, példa API interfészre. Json formát vár, Json formát ad
@app.route('/query', methods=['post'])
def handle_query():
    data = request.json
    string = "Hello " + data.get('name')
    return jsonify({"response": string})

# variable rule
@app.route('/success/<score>') # példa paraméterátadásra, hívás pl /success/55, dynamic URL
def succes(score):
    ##return "The parameter is " + score # egyszerű kiiratás
    return render_template("success.html", result=score) ## ugyanezt Jinja2 templatetel
    ## Jinja2 template elemek HTML-ben
    ## adat resource átadással : {{ result }}
    ## for, loop : {% for key, value in result.item() %}
    ## if : {% if result>=50  %}
if __name__ == "__main__":  # belépési pont
    app.run(debug=True, host='0.0.0.0', port=5001)
