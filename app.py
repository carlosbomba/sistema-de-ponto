from flask import Flask, request, jsonify
from datetime import datetime, timezone
from sqlalchemy_engine import SqlAlchemyDbEngine
from sqlalchemy import select, extract
from point_table import PointTable

app = Flask(__name__)

@app.route("/ponto-adicao", methods=["POST"])
def ponto_adicao():
    tempo = datetime.now()
    usuario = request.json.get('usuario')
    with SqlAlchemyDbEngine() as session:
        new_record = PointTable(
            cnpj_empresa=00000.000,
            matricula=usuario,
            data_ponto=tempo.strftime('%Y-%M-%D'),
            hora_ponto=tempo.strftime('%H:%M:%S')
            )
        session.add(new_record)
        session.commit()
    return "Ponto cadastrado com sucesso!"

@app.route("/busca-ponto", methods=["POST"])
def busca_ponto():
    matricula = request.json.get('matricula')
    month = request.json.get('mes')
    with SqlAlchemyDbEngine() as session:
        tabela_ponto = PointTable
        stmt = (
            select(tabela_ponto.matricula, tabela_ponto.data_ponto, tabela_ponto.hora_ponto, extract("month", tabela_ponto.data_ponto).alias('mes'))
                .where(mes = month)
        )
        stmt_comp = stmt.compile(compile_kwargs={"literal_binds": True})
        results = session.execute(stmt).all()

    return results


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
