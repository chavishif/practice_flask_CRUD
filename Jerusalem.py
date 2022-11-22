from flask import Blueprint

Jerusalem = Blueprint('Jerusalem',__name__,url_prefix='/Jerusalem')

@Jerusalem.route("/museum")
def museum():
    return ("Science Museum")

@Jerusalem.route("/aquarium")
def aquarium():
     return ("Israel Aquarium")

@Jerusalem.route("/zoo")
def zoo():
     return ("Biblical Zoo")