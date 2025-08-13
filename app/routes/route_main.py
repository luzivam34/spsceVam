from flask import Blueprint, render_template

main_bp = Blueprint("main", __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/yugioh')
def yugioh():
    return render_template('yugioh/yugioh.html')

@main_bp.route('/pokemon')
def pokemon():
    return render_template('pokemon/pokemon.html')