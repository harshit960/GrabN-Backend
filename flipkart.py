from itertools import product
import requests
import json

def getFlipkart(keyword):
  products=[]
  jsonoutput={}
  url = 'https://affiliate-api.flipkart.net/affiliate/1.0/search.json?query='+ keyword +'&resultCount=10'

  payload={}
  headers = {
    'Fk-Affiliate-Id': 'harshit960',
    'Fk-Affiliate-Token': '403145a980b743eba1582a1626407ba4'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data=response.json()
  lists = data['products']
  for i in data['products']:
    brand=i['productBaseInfoV1']['productBrand']
    product=i['productBaseInfoV1']['title']
    sp=i['productBaseInfoV1']['flipkartSpecialPrice']['amount']
    originalp=i['productBaseInfoV1']['flipkartSellingPrice']['amount']
    images=i['productBaseInfoV1']['imageUrls']
    image=list(images.values())
    link=i['productBaseInfoV1']['productUrl']
    prodata=json.dumps({'productBrand':brand,'title':product,'flipkartSpecialPrice':sp,'flipkartSellingPrice':originalp, 'imageUrls':image[1],'productUrl':link,'store':'flipkart'})
    products.append(json.loads(prodata))
    
  jsonoutput=json.dumps({'products':products})
  return json.loads(jsonoutput)






 
