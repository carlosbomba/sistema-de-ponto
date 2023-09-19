from flask import Flask, request, jsonify
from datetime import datetime, timezone
from sqlalchemy_engine import SqlAlchemyDbEngine
from point_table import PointTable

app = Flask(__name__)

@app.route("/ponto-adicao", methods=["POST"])
def ponto_adicao():
    tempo = datetime.now()
    usuario = request.json.get('usuario')
    with SqlAlchemyDbEngine() as session:
        tabela_ponto = PointTable
    return "Ponto cadastrado com sucesso!"

@app.route("/busca-ponto", methods=["POST"])
def busca_ponto():
    tempo = datetime.now()
    command = request.json.get('command')
    return str(tempo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
