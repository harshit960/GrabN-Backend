import json
from flask import Flask,jsonify
from flipkart import getflipkartdata
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, harshit</p>"


@app.route("/search/<string:key>")
def search(key):
    data = getflipkartdata(key)
    
    print(type(data))
    return (data)

if __name__=="__main__":
    app.run(debug=True)