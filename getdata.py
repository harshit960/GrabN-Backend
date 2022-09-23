
from functools import total_ordering
from itertools import product
from ajio import getAjio
from flipkart import getFlipkart
from meesho import getMeesho
from myntra import getMynta
from snapdeal import getSnapdeal
from amazon import getAmazon
import json

def final_data(keyword):
    ajio = getAjio(keyword)
    flipkart=getFlipkart(keyword)
    meesho=getMeesho(keyword)
    myntra= getMynta(keyword)
    #snapdael=getSnapdeal(keyword)
    amazon=getAmazon(keyword)
    total =[]
    total.append(json.loads(json.dumps(ajio)))
    total.append(json.loads(json.dumps(flipkart)))
    total.append(json.loads(json.dumps(meesho)))
    total.append(json.loads(json.dumps(myntra)))
    total.append(json.loads(json.dumps(snapdael)))
    #total.append(json.loads(json.dumps(amazon)))
    products=[]
    for i in total:
        for x in i['products']:
            products.append(x)


    return {'products':products}
    
