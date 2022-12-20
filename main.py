from flask import Flask, render_template, json, request

app = Flask(__name__)
from flask import Flask, render_template, json, request, jsonify
from data import *
app = Flask(__name__)

# print(create_table2())

# print(del_table())

# print(add_entry("BeanMann","Juris","Redmanis","Labdien!"))

# print(add_user("JOJO","Jonathan","Jostar"))

@app.route('/get_user')
def passON():
  data = get_user_and_id()
  answer = []
  for element in data:
    answer.append({
    "id":element[0],
    "username":element[1]})
  return jsonify({"all":answer})


@app.route('/register')
def create_page1():
    return render_template("zin.register.html")

@app.route('/pievienot')
def create_page2():
  return render_template("zin.piev.html")

@app.route('/')
def create_page3():
  fullList=[]
  data = getName_and_id() # Dabūt visus vārdus, uzvārdus un ziņas
  for element in data:
    fullList.append({
    "vards":element[0],
    "uzvards":element[1],
    "MSG" : element[2]})# Salikt sarakstā
  return render_template("index.html", visasZinas=fullList)

#Nolasa html->.JS ierakstīto lietotajvardu, vardu un uzvardu un pievieno datubāzei.
@app.route('/enterUSR',methods=["POST"])
def lasit():
  dati=request.json
  print(dati)
  return add_user(dati["username"], dati["vards"], dati["uzvards"])

#Nolasa html->.JS ierakstīto Ziņojumu un Kopā ar izvēlēto lietotāju to pievieno datubāzei.

@app.route('/enterMSG',methods=["POST"])
def lasit2():
  dati=request.json
  print(dati)
  return add_entry(dati["user_id"], dati["zinojums"])

@app.route('/show_msg')
def passMSG():
  data = getName_and_id() 
  Listfull = []
  for element in data:
    Listfull.append({
    "vards":element[0],
    "uzvards":element[1],
    "MSG" : element[2]})
  return ({"all":Listfull})




app.run(host='0.0.0.0', port=81)
