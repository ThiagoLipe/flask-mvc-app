# App de Cadastro em Flask
Aplicativo em Flask utilizando o modelo de arquitetura MVC (Model - View - Controller) de cadastro de nome e email.

#### Funções:
- Adicionar Usuário
- Excluir Usuário
- Visualizar Todos os Usuários Cadastrados

## Técnicas e Tecnologias utilizadas
- ``Python``
- ``Flask``
- ``pip``
- ``sqlalchemy``
- ``HTML``
- ``CSS``

## Requisitos
Antes de tudo é necessário ter instalados em seu computador:
<ul>
  <li><a href="https://www.python.org/downloads/">Python</a></li>
  <li><a href="https://pip.pypa.io/en/stable/installation/">pip</a></li>
  <li><a href="https://git-scm.com/downloads">Git</a></li>
</ul>

# Passos para instalação

## 1. Primeiro clone o repositório
```
git clone https://github.com/ThiagoLipe/flask-mvc-app.git
```

## 2. Abra o arquivo clonado na sua IDE
E abra o terminal cmd na pasta flask-mvc-app

## 3. Crie um ambiente virtual
```python -m venv venv```

## 4. Instalando as bibliotecas
Instale as bibliotecas necessárias, no terminal digite
```
pip install flask
pip install flask_sqlalchemy
```

## 5. Ative o ambiente virtual, ainda no terminal
### Para Windows:
```
venv/Scripts/activate
```
### Para Linux/MacOS:
```
source venv/bin/activate
```

## 6. Defina as variáveis de ambiente, ainda no terminal
### Para Windows:
```
set FLASK_APP=app
set FLASK_ENV=development
```
### Para Linux/MacOS:
```
export FLASK_APP=app
export FLASK_ENV=development
```

## 7. Inicie o banco de dados
```
python init_db.py
```

## 8. Por último, execute o app
```
flask run
```

## Abrir o servidor no seu navegador
Uma porta de servidor será exibida, clique nela para usar o aplicativo.
