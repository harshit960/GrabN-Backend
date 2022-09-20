import json
from flask import Flask,jsonify
from flipkart import getflipkartdata
from sd import ReadAsin
import asyncio

from ajio import getAjio
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, harshit</p>"





@app.route("/search/<string:key>")
async def search(key):
    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    #loop = asyncio.get_event_loop()
    #data = getflipkartdata(key)
    #data2 = ReadAsin()
    data3 = await getAjio(key)
    print(type(data3))
    return (data3)

if __name__=="__main__":
    app.run(debug=True)