from app import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dex = db.Column(db.String(10),nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    typepri = db.Column(db.String(50), nullable=False)
    typesec = db.Column(db.String(50), nullable=True)
    nivel = db.Column(db.Integer, nullable=False)
    hp = db.Column(db.Integer, nullable=False)
    ataque = db.Column(db.Integer, nullable=False)
    defesa = db.Column(db.Integer, nullable=False)
    at_esp = db.Column(db.Integer, nullable=False)
    de_esp = db.Column(db.Integer, nullable=False)
    velocidade = db.Column(db.Integer, nullable=False)
    evolution = db.Column(db.String(100), nullable=False)
    imagem = db.Column(db.String(200))