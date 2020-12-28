from flask import Flask, render_template, redirect, request, url_for
from app import app, db
from app.models import User
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/formacoes')
def index():
    return render_template('formacoes.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if not user or not user.verify_password(password):
            return redirect(url_for('login'))

        login_user(user)
        return render_template('my-cert.html', user=user)

    return render_template('login.html') #form=form)

@app.route('/certificados')

def certificados():
    return render_template('my-cert.html')

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':
        name = request.form['nome']
        email = request.form['email']
        password = request.form['password']

        if name and email and password:
            user = User(name, email, password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route("/logout")
#@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/cadastrar_formacao')
@login_required
def cadastrar_formacao():
    return render_template('cadastrar_formacao.html')
