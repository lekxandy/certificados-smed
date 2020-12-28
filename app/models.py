from datetime import datetime
from app import db, login_manger
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manger.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()

class User(db.Model, UserMixin):
    __tablename = 'users'

    id = db.Column(db.Integer, auto_increment = True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
    
    def __str__(self):
        return self.name


class Formacao(db.Model):
    id = db.Column(db.Integer, auto_increment = True, primary_key=True)
    tema = db.Column(db.String(100), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Date())
    data_de_criacao = db.Column(db.Date(), default = datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    User = db.relationship('User')

    def __str__(self):
        return format("{} - {}", self.tema, self.data)


class Inscricao(db.Model):
    id = db.Column(db.Integer, auto_increment = True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    User = db.relationship('User')
    formacao_id = db.Column(db.Integer, db.ForeignKey('formacao.id'),
        nullable=False)
    formacao = db.relationship('Formacao')
    data_de_inscricao = db.Column(db.Date(), default = datetime.now())