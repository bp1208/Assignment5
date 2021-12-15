from flask import Flask,jsonify, render_template, request, redirect,url_for,escape
import json


app = Flask(__name__,template_folder='templates')
jData = json.loads(open('./pl.json').read())
data=jData["ProgrammingLangauges"]

@app.route('/')
def pl_main():
    return render_template("index.html")

@app.route('/pl/')
def getAllProgrammingLanguages():
    myList=[]
    for element in data:
        myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/pl/<string:Year>/<string:ID>')
def getyearOfPlWithId(Year,ID):
    myList=[]
    for element in data:
        if element["Year"] == Year:
            if element ["ID"] == ID:
                myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)


@app.route('/pl/<string:Year>')
def getyearOfPl(Year):
    myList=[]
    for element in data:
        if element["Year"]== Year:
            myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

@app.route('/pl/<string:Difficulty>/<string:ID>/<string:Price>')
def getPriceOfPl(Difficulty,ID,Price):
    myList=[]
    for element in data:
        if element["Difficulty"]== Difficulty:
            if element ["ID"] == ID:
                if element ['Price'] == Price:
                    myList.append(element)
    result = jsonify(myList)
    return render_template("index.html",items=myList)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')