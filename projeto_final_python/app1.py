from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import requests

app = Flask(__name__)
api = Api(app)

class Cliente(Resource):
    # define os métodos GET, POST, PUT e DELETE
    # para a rota /clientes e /clientes/<int:cliente_id>
    def get(self, cliente_id):
        response = requests.get(f'http://localhost:5001/clientes/{cliente_id}')
        return response.json()

    def post(self):
        data = request.get_json()
        response = requests.post('http://localhost:5001/clientes', json=data)
        return response.json()

    def put(self, cliente_id):
        data = request.get_json()
        response = requests.put(f'http://localhost:5001/clientes/{cliente_id}', json=data)
        return response.json()

    def delete(self, cliente_id):
        response = requests.delete(f'http://localhost:5001/clientes/{cliente_id}')
        return response.json()

# define a rota /score/<int:cliente_id>
# que retorna o score de crédito de um cliente
# baseado no saldo da conta corrente
class ScoreCredito(Resource):
    def get(self, cliente_id):
        response = requests.get(f'http://localhost:5001/clientes/{cliente_id}')
        cliente = response.json()
        score = cliente['saldo_cc'] * 0.1
        return jsonify({'cliente_id': cliente_id, 'score_credito': score})

api.add_resource(Cliente, '/clientes', '/clientes/<int:cliente_id>')
api.add_resource(ScoreCredito, '/score/<int:cliente_id>')

if __name__ == '__main__':
    app.run(port=5000)
