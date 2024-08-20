from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key" # Chave para guardar as informações
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' # Caminho para o banco de dados

login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)
# A sessão armazena nossa conexão ativa e é onde a gente da os comandos
#view login (rota do login)

login_manager.login_view = 'login' #Explicitamos que a rota do login tem o nome login

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id) # resgatar o usuário cadastrado nesse id

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Login

        user = User.query.filter_by(username=username).first() # retorna uma lista e por isso utilizamos o first para pegar só o primeiro

        if user and user.password == password:
            login_user(user) # autenticação do usuário
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso"})
    
    return jsonify({"message": "Credenciais inválidas"}), 400

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})

@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit() #Adição do usuário no banco de dados
        return jsonify({"message": "Usuário cadastrado com sucesso"})


    if username:
        return jsonify({"message": "Senha inválida"}), 400 # Dados incorretos
    
    else:
        return jsonify({"message": "Usuário inválido"})

@app.route('/user/<int:id>', methods=['GET'])
@login_required
def read_user(id):
    user = User.query.get(id)

    if id == current_user.id:
        return jsonify({""})

    if user:
        return {
            "username": user.username
        }

    return jsonify ({"message": "Usuário não encontrado"}), 404

@app.route('/user/<int:id>', methods=['PUT'])
@login_required
def update_user(id):
    user = User.query.get(id)
    data = request.json

    if id == current_user.id:
        return jsonify({"message": "Deleção não permitida"}), 403

    if user and data.get("password"):
       user.password = data.get("password")
       db.session.commit()

       return jsonify({"message": f"Usuário {id} atualizado com sucesso"})
        

    return jsonify ({"message": "Usuário não encontrado"}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
@login_required
def delete_user(id):
    user = User.query.get(id)
    
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": f"Usuário {id} deletado com sucesso"})
    
    return jsonify({"message": "Usuário não encontrado"}), 404








if __name__ == '__main__':
    app.run(debug=True)