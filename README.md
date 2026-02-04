# 🔐 Sample Flask Auth

## 📝 Sobre o projeto

API de autenticação desenvolvida com **Flask** e **Flask-Login**, utilizando banco de dados **MySQL** containerizado com **Docker** para persistência de dados de usuários. O projeto implementa um sistema completo de autenticação com registro, login, logout e gerenciamento de sessões.

Repositório criado para armazenar o código da API de autenticação com banco de dados, demonstrando conceitos essenciais de:
- Sistema de autenticação completo
- Gerenciamento de sessões com Flask-Login
- Persistência de dados com SQLAlchemy e MySQL
- Containerização com Docker
- Criptografia de senhas
- ORM (Object-Relational Mapping)

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask 2.3.0** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **Flask-Login 0.6.2** - Gerenciamento de autenticação e sessões
- **MySQL** - Banco de dados relacional
- **Docker** - Containerização do banco de dados
- **PyMySQL 1.1.0** - Conector MySQL para Python
- **Werkzeug 2.3.0** - WSGI toolkit e criptografia
- **Cryptography 41.0.7** - Biblioteca de criptografia

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- Docker e Docker Compose instalados
- pip (gerenciador de pacotes Python)

### Configuração do Banco de Dados com Docker

1. Inicie o container MySQL usando Docker Compose:
```bash
docker-compose up -d
```

2. Verifique se o container está rodando:
```bash
docker ps
```

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

### Parando os serviços
```bash
# Parar o container MySQL
docker-compose down

# Parar e remover volumes (apaga os dados)
docker-compose down -v
```

## 🐳 Configuração do Docker

### Credenciais do MySQL (docker-compose.yml)
```yaml
MYSQL_USER: admin
MYSQL_PASSWORD: admin123
MYSQL_DATABASE: flask-crud
MYSQL_ROOT_PASSWORD: admin123
```

### Conexão da aplicação
```python
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:admin123@localhost:3306/flask-crud'
```

## 🎯 Funcionalidades

- 📝 **Registro de usuários** com validação de dados
- 🔑 **Login** com autenticação segura
- 🚪 **Logout** para encerrar sessão
- 🔒 **Rotas protegidas** que requerem autenticação
- 👤 **Gerenciamento de sessões** com Flask-Login
- 💾 **Persistência de dados** em MySQL via Docker
- 🔐 **Criptografia de senhas** com Werkzeug
- 🐳 **Banco de dados containerizado**

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
- **Docker**: Isolamento do banco de dados

## 🗃️ Estrutura do Banco de Dados

O projeto utiliza **MySQL containerizado com Docker**, garantindo:
- Ambiente isolado e reproduzível
- Fácil configuração e deploy
- Persistência de dados em volumes
- Portabilidade entre ambientes
- Integridade referencial
- Transações ACID

## 🐳 Comandos úteis do Docker
```bash
# Iniciar os containers
docker-compose up -d

# Ver logs do MySQL
docker-compose logs db

# Acessar o MySQL via linha de comando
docker exec -it  mysql -u admin -p

# Parar os containers
docker-compose down

# Reiniciar os containers
docker-compose restart
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
