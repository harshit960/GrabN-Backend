
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
    total =[]

    try:
        amazon=getAmazon(keyword)
        total.append(json.loads(json.dumps(amazon)))
    except:
        print('amazon 503')
    try:
        flipkart=getFlipkart(keyword)
        total.append(json.loads(json.dumps(flipkart)))
    except:
        print('flipkart 503')
    #meesho=getMeesho(keyword)
    try:
        myntra= getMynta(keyword,1)
        total.append(json.loads(json.dumps(myntra)))
    except:
        print('myntra 503')


    #snapdael=getSnapdeal(keyword)
    try:
        ajio = getAjio(keyword)
        total.append(json.loads(json.dumps(ajio)))
    except:
        print('ajio 503')
    #total.append(json.loads(json.dumps(meesho)))
    
    #total.append(json.loads(json.dumps(snapdael)))
    
    products=[]
    for i in total:
        for x in i['products']:
            products.append(x)


    return {'products':products}
    
