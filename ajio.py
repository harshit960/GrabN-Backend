
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import os
import time
def getAjio(keyword):
    products=[]
    jsonoutput={}
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    option = webdriver.ChromeOptions()
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    option.add_argument("--headless")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=option)
    #option.headless=True
    #option.add_argument('--headless')
    #option.add_argument(f'user-agent={user_agent}')
    #option.add_argument("--ignore-certificate-error")
    #option.add_argument("--ignore-ssl-errors"
    
    #PATH ="C:\Program Files (x86)\chromedriver.exe"
    #driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.ajio.com/search/?query=%3Arelevance&text="+ keyword +"&classifier=intent&customerType=New&gridColumns=5")
    
    for i in range(40):
        driver.execute_script("window.scrollBy(0,400)","")
        time.sleep(0.01)
    
    
    items =driver.find_elements(By.CLASS_NAME,"rilrtl-products-list__item")
    for item in items:
        imageraw=item.find_elements(By.CLASS_NAME, "rilrtl-lazy-img")
        if imageraw[0].get_attribute('src') == None:
            break
        else:
            image=imageraw[0].get_attribute('src')
        brand=item.find_element(By.CLASS_NAME, "brand").text
        product=item.find_element(By.CLASS_NAME, "nameCls").text
        sp=item.find_element(By.CLASS_NAME, "price").text
        try:
            originalp=item.find_element(By.CSS_SELECTOR, "div > span.orginal-price").text
        except:
            pass
        link=item.find_element(By.CLASS_NAME, "rilrtl-products-list__link").get_attribute("href")
        #prodata=json.dumps({'productBrand':brand,'title':product,'sp':sp, 'photo':image,'link':link})
        prodata=json.dumps({'productBrand':brand,'title':product,'flipkartSpecialPrice':sp,'flipkartSellingPrice':originalp, 'imageUrls':image,'productUrl':link,'store':'Ajio'})
        products.append(json.loads(prodata))
    driver.close()
    jsonoutput=json.dumps({'products':len(products)})
    return json.loads(jsonoutput)

