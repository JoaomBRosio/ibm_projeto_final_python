from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
api = Api(app)

DATABASE_URL = "sqlite:///projeto_final_python/bd/clientes.db"

# certifica que o diretório do banco de dados existe
os.makedirs(os.path.dirname(DATABASE_URL.split("///")[1]), exist_ok=True)

# cria o banco de dados
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# cria a tabela de clientes
class ClienteModel(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    telefone = Column(Integer)
    correntista = Column(Boolean)
    score_credito = Column(Float)
    saldo_cc = Column(Float)

# cria a tabela no banco de dados
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# insere dados na tabela
class Cliente(Resource):
    def get(self, cliente_id=None):
        if cliente_id:
            # busca o cliente pelo id
            cliente = session.query(ClienteModel).filter_by(id=cliente_id).first()
            if cliente:
                # retorna o cliente encontrado
                return jsonify({
                    'id': cliente.id,
                    'nome': cliente.nome,
                    'telefone': cliente.telefone,
                    'correntista': cliente.correntista,
                    'score_credito': cliente.score_credito,
                    'saldo_cc': cliente.saldo_cc
                })
            return {'message': 'Cliente não encontrado'}, 404
        else:
            # busca todos os clientes
            clientes = session.query(ClienteModel).all()
            return jsonify([{
                'id': cliente.id,
                'nome': cliente.nome,
                'telefone': cliente.telefone,
                'correntista': cliente.correntista,
                'score_credito': cliente.score_credito,
                'saldo_cc': cliente.saldo_cc
            } for cliente in clientes])

    # insere um novo cliente
    def post(self):
        data = request.get_json()
        score_credito = data['saldo_cc'] * 0.1
        novo_cliente = ClienteModel(
            nome=data['nome'],
            telefone=data['telefone'],
            correntista=data['correntista'],
            score_credito=score_credito,
            saldo_cc=data['saldo_cc']
        )
        # adiciona o novo cliente ao banco de dados
        session.add(novo_cliente)
        session.commit()
        return jsonify({
            'id': novo_cliente.id,
            'nome': novo_cliente.nome,
            'telefone': novo_cliente.telefone,
            'correntista': novo_cliente.correntista,
            'score_credito': novo_cliente.score_credito,
            'saldo_cc': novo_cliente.saldo_cc
        })

    # atualiza um cliente
    def put(self, cliente_id):
        cliente = session.query(ClienteModel).filter_by(id=cliente_id).first()
        if cliente:
            data = request.get_json()
            cliente.nome = data['nome']
            cliente.telefone = data['telefone']
            cliente.correntista = data['correntista']
            cliente.saldo_cc = data['saldo_cc']
            cliente.score_credito = data['saldo_cc'] * 0.1
            session.commit()
            # retorna o cliente atualizado
            return jsonify({
                'id': cliente.id,
                'nome': cliente.nome,
                'telefone': cliente.telefone,
                'correntista': cliente.correntista,
                'score_credito': cliente.score_credito,
                'saldo_cc': cliente.saldo_cc
            })
        return {'message': 'Cliente não encontrado'}, 404


    def delete(self, cliente_id):
        cliente = session.query(ClienteModel).filter_by(id=cliente_id).first()
        if cliente:
            session.delete(cliente)
            session.commit()
            return {'message': 'Cliente deletado'}
        return {'message': 'Cliente não encontrado'}, 404

# adiciona a rota /clientes
api.add_resource(Cliente, '/clientes', '/clientes/<int:cliente_id>')

# roda a aplicação
if __name__ == '__main__':
    app.run(port=5001)
