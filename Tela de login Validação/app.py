from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Caminho para o arquivo JSON
JSON_FILE = 'users.json'

# Função para ler o arquivo JSON
def read_users():
    if not os.path.exists(JSON_FILE):
        return {}
    with open(JSON_FILE, 'r') as file:
        return json.load(file)

# Função para escrever no arquivo JSON
def write_users(users):
    with open(JSON_FILE, 'w') as file:
        json.dump(users, file, indent=4)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = data.get('user')
    password = data.get('password')

    users = read_users()

    if user in users and users[user] == password:
        return jsonify({'status': 'success', 'message': 'Login bem-sucedido!'})
    else:
        return jsonify({'status': 'error', 'message': 'Usuário ou senha incorretos!'})

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    user = data.get('user')
    password = data.get('password')
    password_confirm = data.get('password_confirm')

    # Verifica se as senhas coincidem
    if password != password_confirm:
        return jsonify({'status': 'error', 'message': 'As senhas não coincidem!'})

    users = read_users()

    # Verifica se o usuário já existe
    if user in users:
        return jsonify({'status': 'error', 'message': 'Usuário já existe!'})

    # Adiciona o novo usuário ao dicionário e escreve no arquivo
    users[user] = password
    write_users(users)

    return jsonify({'status': 'success', 'message': 'Cadastro bem-sucedido!'})

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
