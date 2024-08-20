from database import db
from flask_login import UserMixin # classe de usuário já pronta do Flask

class User(db.Model, UserMixin): #Usamos isso para o flask reconhecer essa classe como algo mapeável
    # id, username, senha (o que iremos armazenar)
    id = db.Column(db.Integer, primary_key=True) # temos várias colunas no db que depende do tipo que queremos armazenar (Ex: integers, strings, float...)
    # Quando usamos a primary_key=True estamos dizendo que essa é a minha chave primária (identifica os registros na tabela e é uma chave única) da tabela de usuários
    # É através dela que realizamos a consulta de dados específicos
    username = db.Column(db.String(80), nullable=False, unique=True) # nullable é um booleano para dizermos se aceitamos essa coluna estar vazia ou não e o unique é um boolenao para saber se aquela coluna é única
    password = db.Column(db.String(80), nullable=False)