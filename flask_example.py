"""
Flask: API végpont

Lekérdezés: 
curl -X POST "http://127.0.0.1:5001/query" \
     -H "Content-Type: application/json" \
     -d '{"name":"Tom","age":"32"}'
"""

from flask import Flask, request, jsonify
app = Flask(__name__)

# Felhasználói kérdés feldolgozása
@app.route('/hello', methods=['get'])
def handle_hello_get():
    return "Hello World"

# Felhasználói kérdés feldolgozása
@app.route('/query', methods=['post'])
def handle_query():
    data = request.json
    string = "Hello " + data.get('name')
    return jsonify({"response": string})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
