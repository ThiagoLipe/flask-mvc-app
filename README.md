# App de Cadastro em Flask
Aplicativo em flask utilizando o modelo de arquitetura MVC (Model - View - Controller) de cadastro de nome e email.

#### Funções:
- Adicionar Usuário
- Excluir Usuário
- Visualizar todos os Usuários cadastrados

## Técnicas e Tecnologias utilizadas
- ''Python''
- ''Flask''
- ''pip''
- ''sqlalchemy''
- ''HTML''
- ''CSS''

## Requisitos
Antes de tudo é necessário ter as seguintes instalações:
<ul>
  <li><a href="https://www.python.org/downloads/">Python</a></li>
  <li><a href="https://pip.pypa.io/en/stable/installation/">pip</a></li>
  <li><a herf="https://git-scm.com/downloads">Git</a></li>
</ul>

# Passos para instalação
## 1. Primeiro clone o repositório
'''
git clone https://github.com/ThiagoLipe/flask-mvc-app.git
'''

## 2.Abra o arquivo clonado na sua IDE
<p>E acesse o terminal</p>

## 3.Instalando as bibliotecas
<p>Instale as bibliotecas necessárias, no terminal digite</p>
'''
pip install Flask
pip install flask_sqlalchemy
'''

## 4. Ative o ambiente virtual, ainda no terminal
### Para Windows:
'''
venv/Scripts/activate
'''

### Para Linux/MacOS:
'''
source venv/bin/activate
'''

## 5. Defina as variáveis de ambiente, ainda no terminal
### Para Windows:
'''
set FLASK_APP=app
set FLASK_ENV=development
'''

### Para Linux/MacOS:
'''
export FLASK_APP=app
export FLASK_ENV=development
'''

## 6. Inicie o banco de dados
'''
python init_db.py
'''

## 7. Por último, execute o app
'''
flask run
'''

## Abrir o servidor no seu navegador
Uma porta de servidor será exibida, clique nela para usar o aplicativo.
