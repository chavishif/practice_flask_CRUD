from flask import Flask, render_template,request
from haifa import haifa
from Jerusalem import Jerusalem
from telaviv import telaviv


app = Flask(__name__)
app.register_blueprint(haifa)
app.register_blueprint(Jerusalem)
app.register_blueprint(telaviv)

Attraction_h = [{"Attraction":"Cable-Car"},{"Attraction":"Habyim"},{"Attraction":"ninja"}]
Attraction_t = [{"Attraction":"Luna-Park"},{"Attraction":"Museum of Illusions"},{"Attraction":"laser tag"}]
Attraction_j = [{"Attraction":"Science Museum"},{"Attraction":"Israel Aquarium"},{"Attraction":"Biblical Zoo"}]

@app.route('/<id>')
@app.route('/')
def haifa_attrac(id=0):
    return render_template('haifaH.html',ar=f'/static/images/h{id}.jpg',myar=Attraction_h[int(id)])

@app.route('/telaviv/<id>')
@app.route('/telaviv')
def telaviv_attrac(id=0):
    return render_template('TelAvivH.html',ar=f'/static/images/t{id}.jpg',myar=Attraction_t[int(id)])

@app.route('/Jerusalem/<id>')
@app.route('/Jerusalem')
def jerusalem_attrac(id=0):
    return render_template('JerusalemH.html',ar=f'/static/images/j{id}.jpg',myar=Attraction_j[int(id)])


students = ["aviv","noa","gil"]

@app.route('/petachtikva')
def all():
    return f'hello{(students)}'

@app.route('/petachtikva/add',methods=['post'])
def add_students():
    new_student=request.get_json()["stuname"]
    students.append(new_student)
    return f'hello{(students)}'