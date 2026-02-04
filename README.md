# 🔐 Sample Flask Auth

## 📝 Sobre o projeto

API de autenticação desenvolvida com **Flask** e **Flask-Login**, utilizando banco de dados **MySQL** para persistência de dados de usuários. O projeto implementa um sistema completo de autenticação com registro, login, logout e gerenciamento de sessões.

Repositório criado para armazenar o código da API de autenticação com banco de dados, demonstrando conceitos essenciais de:
- Sistema de autenticação completo
- Gerenciamento de sessões com Flask-Login
- Persistência de dados com SQLAlchemy e MySQL
- Criptografia de senhas
- ORM (Object-Relational Mapping)

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask 2.3.0** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **Flask-Login 0.6.2** - Gerenciamento de autenticação e sessões
- **MySQL** - Banco de dados relacional
- **PyMySQL 1.1.0** - Conector MySQL para Python
- **Werkzeug 2.3.0** - WSGI toolkit e criptografia
- **Cryptography 41.0.7** - Biblioteca de criptografia

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- MySQL instalado e rodando
- pip (gerenciador de pacotes Python)

### Configuração do Banco de Dados

1. Crie um banco de dados MySQL:
```sql
CREATE DATABASE flask_auth;
```

2. Configure as credenciais de acesso no arquivo de configuração da aplicação

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/sample-flask-auth.git
cd sample-flask-auth
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executando a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## 🎯 Funcionalidades

- 📝 **Registro de usuários** com validação de dados
- 🔑 **Login** com autenticação segura
- 🚪 **Logout** para encerrar sessão
- 🔒 **Rotas protegidas** que requerem autenticação
- 👤 **Gerenciamento de sessões** com Flask-Login
- 💾 **Persistência de dados** em MySQL
- 🔐 **Criptografia de senhas** com Werkzeug

## 🛠️ Modelo de dados

### User (Usuário)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto-incremento) |
| username | String | Nome de usuário (único) |
| email | String | E-mail do usuário (único) |
| password | String | Senha criptografada |
| created_at | DateTime | Data de criação da conta |

## 📸 Endpoints da API

### Autenticação

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/register` | Registra um novo usuário | Não |
| POST | `/login` | Autentica usuário e cria sessão | Não |
| POST | `/logout` | Encerra a sessão do usuário | Sim |
| GET | `/profile` | Retorna dados do usuário logado | Sim |

## 💡 Exemplos de uso

### Registrar um novo usuário
```bash
POST /register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "message": "Usuário registrado com sucesso",
  "user_id": 1
}
```

### Fazer login
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "message": "Login realizado com sucesso",
  "user": {
    "id": 1,
    "username": "johndoe",
    "email": "john@example.com"
  }
}
```

### Acessar perfil (rota protegida)
```bash
GET /profile
Cookie: session=...
```

**Resposta:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00"
}
```

### Fazer logout
```bash
POST /logout
Cookie: session=...
```

**Resposta:**
```json
{
  "message": "Logout realizado com sucesso"
}
```

## 🔒 Recursos de Segurança

- **Werkzeug Security**: Hash de senhas com salt
- **Flask-Login**: Gerenciamento seguro de sessões
- **SQLAlchemy**: Proteção contra SQL Injection
- **Validação de dados**: Verificação de entrada do usuário
- **Sessões criptografadas**: Cookies seguros

## 🗃️ Estrutura do Banco de Dados

O projeto utiliza **MySQL** como banco de dados relacional, garantindo:
- Persistência de dados
- Integridade referencial
- Transações ACID
- Performance otimizada para queries

## ⚠️ Configuração

Certifique-se de configurar as seguintes variáveis antes de executar:
```python
# Configurações do banco de dados
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost/flask_auth'
SECRET_KEY = 'sua_chave_secreta_aqui'
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
