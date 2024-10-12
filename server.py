from flask import Flask, request

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def alert():
    data = request.json
    print(f"Alerta recibida: {data}")
    return "Alerta recibida", 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)