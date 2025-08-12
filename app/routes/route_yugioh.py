import os
from flask import Blueprint, render_template, redirect, url_for, request, current_app
from app.models.modcards import Cardmonsternormal
from app import db
from werkzeug.utils import secure_filename

yugioh_bp = Blueprint('yugioh', __name__)

cdmn = Cardmonsternormal

@yugioh_bp.route('/yugiohcard')
def yugiohcards():
    

    cardmonstro = cdmn.query.order_by(cdmn.nome).all()
    return render_template('yugioh/yugiohcards.html', cardmonstro=cardmonstro)

@yugioh_bp.route('/cadastro/card', methods=['POST', 'GET'])
def cadastro_cards():
    if request.method == 'POST':
        nome = request.form['nome']
        atributo = request.form['atributo']
        nivel = request.form['nivel']
        typemonster = request.form['typemonster']
        typecard = request.form['typecard']
        ataque = request.form['ataque']
        defesa = request.form['defesa']

        imagem = request.files['imagem']
        imagem_file = None
        if imagem:
            filename = secure_filename(imagem.filename)
            imagem_folder = os.path.join(current_app.root_path, 'static/uploads')
            os.makedirs(imagem_folder, exist_ok=True)
            imagem.save(os.path.join(imagem_folder, filename))
            imagem_file = f'uploads/{filename}'

        card = cdmn(nome=nome, atributo=atributo, nivel=nivel, typemonster=typemonster, typecard=typecard, ataque=ataque, defesa=defesa, imagem=imagem_file)
        db.session.add(card)
        db.session.commit()

        return redirect(url_for('yugioh.yugiohcards'))
    return render_template('yugioh/cadastro_cards.html')
