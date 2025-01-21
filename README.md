# Banco Javer

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

Banco Javer é uma aplicação desenvolvida em Python utilizando o framework Flask. Este projeto foi criado para operações de gerenciamento de clientes e possui as seguintes funcionalidades:

- Cadastrar cliente
- Buscar todos os clientes
- Buscar cliente por id
- Atualizar cliente
- Deletar cliente
- Calcular score de crédito

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para desenvolver a aplicação.
- **Flask**: Framework que facilita a criação de aplicações web em Python.
- **SQLite**: Banco de dados utilizado para armazenamento de dados localmente.
- **VS Code**: IDE utilizada para o desenvolvimento do projeto.

## Executando a Aplicação

### Pré-requisitos

- Python 3.13.1
- Flask
- Flask-RESTful
- SQLAlchemy
- Requests

### Passos para executar a aplicação

1. Clone o repositório:
    ```bash
    git clone https://github.com/JoaomBRosio/ibm_projeto_final_python
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd diretorioDoProjeto
    ```
3. Inicie a primeira aplicação:
    ```bash
    python app1.py
    ```
4. Inicie a segunda aplicação em outro terminal:
    ```bash
    python app2.py
    ```

### Passos para usar e testar a aplicação

Com ambas as aplicações rodando, você pode usar uma ferramenta como o Postman para testar as APIs.

- Para cadastrar um novo cliente, faça uma requisição POST para `http://localhost:5001/clientes` com o seguinte JSON:
  ```json
  {
     "nome": "Nome de cliente",
     "telefone": 123456789,
     "correntista": true,
     "saldo_cc": 90000.50
  }
  ```
- Para buscar todos os clientes, faça uma requisição GET para `http://localhost:5001/clientes`.
- Para buscar um cliente por ID, faça uma requisição GET para `http://localhost:5001/clientes/1`.
- Para atualizar um cliente, faça uma requisição PUT para `http://localhost:5001/clientes/1` com o seguinte JSON:
  ```json
  {
     "nome": "Nome atualizado",
     "telefone": 123456789,
     "correntista": true,
     "saldo_cc": 90000.50
  }
  ```
- Para deletar um cliente, faça uma requisição DELETE para `http://localhost:5001/clientes/1`.
- Para calcular o score de crédito de um cliente, faça uma requisição GET para `http://localhost:5000/score/1`.

E foi assim que solucionei o problema com Python. Espero que tenha gostado.

João Ambrósio
