

import re
from flask import Flask,jsonify
from getdata import final_data
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, harshit</p>"

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s



@app.route("/search/<string:key>/<int:page>")
def search(key,page):
    key=slugify(key)
    data =final_data(key,page)
    return (data)

if __name__=="__main__":
    app.run(debug=True)