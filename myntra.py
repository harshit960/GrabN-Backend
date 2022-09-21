
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

def getajio(keyword):
    products=[]
    jsonoutput={}
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument("--ignore-certificate-error")
    option.add_argument("--ignore-ssl-errors")
    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.myntra.com/boat")
    
    items =driver.find_elements(By.CLASS_NAME,"rilrtl-products-list__item")
    for item in items:
        imageraw=item.find_elements(By.CLASS_NAME, "rilrtl-lazy-img-loaded")
        if len(imageraw) == 0:
            break
        else:
            image=imageraw[0].get_attribute('src')
        brand=item.find_element(By.CLASS_NAME, "brand").text
        product=item.find_element(By.CLASS_NAME, "nameCls").text
        sp=item.find_element(By.CLASS_NAME, "price").text
        originalp=item.find_element(By.CLASS_NAME, "orginal-price").text
        
        link=item.find_element(By.CLASS_NAME, "rilrtl-products-list__link").get_attribute("href")
        prodata=json.dumps({'brand':brand,'name':product,'sp':sp, 'photo':image,'link':link})
        products.append(json.loads(prodata))
    driver.close()
    jsonoutput=json.dumps({'products':products})
    return json.loads(jsonoutput)
    
