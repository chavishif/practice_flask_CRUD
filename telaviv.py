from flask import Blueprint

telaviv = Blueprint('telaviv',__name__,url_prefix='/telaviv')

@telaviv.route("/luna")
def luna():
    return ("Luna-Park")

@telaviv.route("/museum")
def museum():
     return ("Museum of Illusions")

@telaviv.route("/lazer")
def lazer():
     return ("laser tag")
