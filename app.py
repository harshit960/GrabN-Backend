

import re
from flask import Flask,jsonify
from getdata import final_data
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
    data =final_data(key)
    return (data)

if __name__=="__main__":
    app.run(debug=True)