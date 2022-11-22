from flask import Blueprint,render_template

haifa = Blueprint('haifa',__name__,url_prefix='/')

@haifa.route("/cableCar")
def cablecar():
    return ("cablecar")

@haifa.route("/habyim")
def habyim():
     return ("habyim")

@haifa.route("/ninja")
def ninja():
     return ("ninja")
