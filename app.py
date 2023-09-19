from flask import Flask, request, jsonify
from datetime import datetime, timezone


app = Flask(__name__)

@app.route("/ponto-adicao", methods=["POST"])
def ponto_adicao():
    tempo = datetime.now()
    # usuario = request.json.get('usuario')
    return "Ponto cadastrado com sucesso!"

@app.route("/busca-ponto", methods=["POST"])
def busca_ponto():
    tempo = datetime.now()
    command = request.json.get('command')
    return str(tempo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
