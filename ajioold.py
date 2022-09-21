
from requests_html import AsyncHTMLSession
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor



async def getAjio(keyword):
    asession = AsyncHTMLSession()
    products=[]
    jsonoutput={}
    url = 'https://www.ajio.com/search/?query=%3Arelevance&text='+keyword+'&classifier=intent&customerType=New&gridColumns=5'
    r = await asession.get(url)
    await r.html.arender(sleep=0, keep_page=True, scrolldown=10, timeout=20)
    item =await  r.html.find('.rilrtl-products-list__item')
    for x in item:
        thumbnail = x.find('.rilrtl-lazy-img-loaded')
        if len(thumbnail)==0:
            break
        else:
            img = thumbnail[0].xpath('//img')[0]
            

            brand = x.find('.brand')[0]
            
            product = x.find('.nameCls')[0]
            
            sp = x.find('.price')[0]
            
            originalp = x.find('.orginal-price')[0]
            
        
            link = x.find('.rilrtl-products-list__link')[0]
            
            prodata=json.dumps({'brand':brand.text,'name':product.text,'sp':sp.text, 'photo':img.attrs['src'],'link':list(link.absolute_links)})
            products.append(json.loads(prodata))
    
    jsonoutput=json.dumps({'products':products})
    await asession.close()
    return json.loads(jsonoutput)

            
