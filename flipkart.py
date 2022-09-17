import requests


def getflipkartdata(keyword):
  url = 'https://affiliate-api.flipkart.net/affiliate/1.0/search.json?query='+ keyword

  payload={}
  headers = {
    'Fk-Affiliate-Id': 'harshit960',
    'Fk-Affiliate-Token': '403145a980b743eba1582a1626407ba4'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  data=response.json()
  return data
 
 
 #print(getflipkartdata(keyword))