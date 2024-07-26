from flask import render_template, request, redirect, url_for
from app import app
from app.controllers import add_user, get_all_users, delete_user

@app.route('/')
def index():
    return redirect(url_for('list_users'))

@app.route('/add', methods=['GET', 'POST'])
def add_user_view():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        add_user(name, email)
        return redirect(url_for('list_users'))
    return render_template('add.html')

@app.route('/list')
def list_users():
    users = get_all_users()
    return render_template('list.html', users=users)

@app.route('/delete/<int:user_id>', methods=['GET'])
def delete_user_view(user_id):
    delete_user(user_id)
    return redirect(url_for('list_users'))