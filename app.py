import json
import re
from flask import Flask,jsonify
from flipkart import getflipkartdata
from sd import ReadAsin
from ajio import getajio
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, harshit</p>"

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s



@app.route("/search/<string:key>")
def search(key):
    key=slugify(key)
    data = getflipkartdata(key)
    #data2 = ReadAsin()
    #data3 = getajio(key)
    return (data)

if __name__=="__main__":
    app.run(debug=True)