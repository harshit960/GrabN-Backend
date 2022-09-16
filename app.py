from ast import While
from itertools import product
from flask import Flask,jsonify
from searchresults import getSearchdata
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, harshit</p>"


@app.route("/search/<string:key>")
def search(key):
    while(True):
        if getSearchdata(key) != None:
            data=getSearchdata(key)
            break

    products=data["products"]
    return jsonify(products)

if __name__=="__main__":
    app.run(debug=True)