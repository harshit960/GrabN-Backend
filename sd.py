from bs4 import BeautifulSoup
import re
import requests
import json

def snapdealparser(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    htmltext = response.text
    soup = BeautifulSoup(htmltext,'html.parser')
    try:
        namelist=soup.findAll('img',{'class':"cloudzoom"})
        name = namelist[0].get('title')
        price = soup.find('span',{'class':"payBlkBig"})
        rating = soup.find('span',{'class':"avrg-rating"})
        photo = soup.findAll('img',{'class':"cloudzoom"})[0].get('src')
        link = url
        output=json.dumps({'name':name,'price':price.text,'rating':rating.text, 'photo':photo,'link':link})
        return json.loads(output)
    except:
        pass

def getproductid():
    url = "https://www.snapdeal.com/search?keyword=tshirt"
    print("Searching your product at...",url,sep=" ")
    htmltext = requests.get(url).text
    pattern = re.compile(r"/product/.*/\d{12,12}")  #Snapdeal product id
    List = re.findall(pattern,htmltext)
    List = list(set(List))
    return List

def ReadAsin():
    
    Id = getproductid()
    extracted_data = []
    jsonoutput={}
    for i in Id:
        url = "https://www.snapdeal.com"+i
        print ("Processing: "+url)
        extracted_data.append(snapdealparser(url))

    jsonoutput=json.dumps({'products':extracted_data})
    return json.loads(jsonoutput)
        
