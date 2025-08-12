from app import db


class Cardmonsternormal(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.String(100), nullable=False)
    atributo = db.Column(db.String(20), nullable=False)
    nivel = db.Column(db.Integer, nullable=False)
    typemonster = db.Column(db.String(50), nullable=False) 
    typecard = db.Column(db.String(50), nullable=False)
    ataque = db.Column(db.Integer, nullable=False )
    defesa = db.Column(db.Integer, nullable=False )
    imagem = db.Column(db.String(200))


