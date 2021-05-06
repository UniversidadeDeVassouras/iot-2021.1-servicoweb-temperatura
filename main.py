from flask import Flask, jsonify, request
from datetime import datetime
from temperatura import Temperatura

temperatura_list = [Temperatura(1, 1, 34.5, datetime.now()), Temperatura(2, 1, 34.5, datetime.now()),
                    Temperatura(3, 2, 34.5, datetime.now())]

app = Flask(__name__)


@app.route("/temperatura", methods=['GET'])
def list_temperatura():
    temperatura_dict_list = []
    for temperatura in temperatura_list:
        temperatura_dict_list.append(temperatura.toDict())
    return jsonify(temperatura_dict_list)


@app.route("/temperatura", methods=['POST'])
def add_temperatura():
    id = len(temperatura_list) + 1
    data = datetime.strptime(request.json['data'], '%d/%m/%Y %H:%M')
    dispositivo_id = int(request.json['dispositivo_id'])
    valor = float(request.json['valor'])
    temperatura = Temperatura(id, dispositivo_id, valor, data)
    temperatura_list.append(temperatura)
    return temperatura.toDict(), 201


@app.route("/temperatura/<int:id>", methods=['GET'])
def view_temperatura(id: int):
    for temperatura in temperatura_list:
        if temperatura.id == id:
            return temperatura.toDict()
    return jsonify({"error": "Temperatura não encontrada"}), 404


@app.route("/temperatura/<int:id>", methods=['PUT'])
def edit_temperatura(id: int):
    data = datetime.strptime(request.json['data'], '%d/%m/%Y %H:%M')
    dispositivo_id = int(request.json['dispositivo_id'])
    valor = float(request.json['valor'])
    for temperatura in temperatura_list:
        if temperatura.id == id:
            temperatura.dispositivo_id = dispositivo_id
            temperatura.valor = valor
            temperatura.data = data
            return temperatura.toDict()
    return jsonify({"error": "Temperatura não encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)
