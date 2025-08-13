from flask import Blueprint, render_template, redirect,request, url_for, current_app
import os
from werkzeug.utils import secure_filename
from app import db
from app.models.modpokemon import Pokemon
from sqlalchemy import desc

pokemon_bp = Blueprint('pokemon', __name__)

@pokemon_bp.route('/pokemon_list')
def list_pokemon():
    pokemon = Pokemon.query.order_by(desc(Pokemon.nivel)).all()
    return render_template('pokemon/pokemon_list.html',pokemon=pokemon)

@pokemon_bp.route('/pokemon/<int:id>')
def show_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    return render_template('pokemon/pokemonshow.html', pokemon=pokemon)

@pokemon_bp.route("/cadastrar/pokemon", methods=['POST','GET'])
def cadastra_poquemon():
    if request.method == 'POST':
        nome = request.form['nome']
        dex = request.form['dex']
        typepri = request.form['typepri']
        typesec = request.form['typesec']
        nivel = request.form['nivel']
        hp = request.form['hp']
        ataque = request.form['ataque']
        defesa = request.form['defesa']
        at_esp = request.form['at_esp']
        de_esp= request.form['de_esp']
        velocidade= request.form['velocidade']
        evolution = request.form['evolution']
        imagem = request.files['imagem']
        imagem_file = None

        if imagem:
            filename = secure_filename(imagem.filename)
            imagem_folder = os.path.join(current_app.root_path, 'static/uploads/pokemons')
            os.makedirs(imagem_folder, exist_ok=True)
            imagem.save(os.path.join(imagem_folder, filename))
            imagem_file = f'uploads/pokemons/{filename}'

        pokemon = Pokemon(nome=nome, dex=dex, typepri=typepri, typesec=typesec, nivel=nivel, hp=hp, ataque=ataque, defesa=defesa, at_esp=at_esp, de_esp=de_esp, velocidade=velocidade, evolution=evolution, imagem=imagem_file)
        db.session.add(pokemon)
        db.session.commit()

        return redirect(url_for('pokemon.list_pokemon'))
    
    return render_template('pokemon/cadastrarpokemon.html')

@pokemon_bp.route('/pokemon/excluir/<int:id>', methods=['POST','GET'])
def excluir_pokemon(id):
    pokemon = Pokemon.query.get_or_404(id)
    db.session.delete(pokemon)
    db.session.commit()
    return redirect(url_for('pokemon.list_pokemon'))