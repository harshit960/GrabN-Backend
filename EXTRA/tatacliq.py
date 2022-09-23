
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

def getTataCliq():
    products=[]
    jsonoutput={}
    user_agent ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36"
    option = webdriver.ChromeOptions()
    option.headless=True
    #option.add_argument('--headless')
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("--ignore-certificate-error")
    option.add_argument("--ignore-ssl-errors")
    option.add_argument('--no-sandbox')
    #option.add_argument('--start-maximized')
    #option.add_argument('--start-fullscreen')
    option.add_argument('--single-process')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument("--incognito")
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('--disable-blink-features=AutomationControlled')
    #option.add_experimental_option('useAutomationExtension', False)
    #option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument("disable-infobars")


    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.tatacliq.com/search/?searchCategory=all&text=boat")

    for i in driver.find_elements(By.CLASS_NAME,"Grid__displayInline"):
        items =i.find_elements(By.CLASS_NAME,"Grid__element")
        for item in items:
            imageraw=item.find_elements(By.CLASS_NAME, "Image__actual")
            if len(imageraw) == 0:
                break
            else:
                image=imageraw[0].get_attribute('src')
            brand=item.find_element(By.CLASS_NAME, "ProductDescription__boldText").text
            product=item.find_element(By.CLASS_NAME, "ProductDescription__description  ").text
            sp=item.find_element(By.CLASS_NAME, "ProductDescription__boldText").text
            originalp=item.find_element(By.CLASS_NAME, "ProductDescription__priceCancelled").text
            
            link=item.find_element(By.CLASS_NAME, "ProductModule__aTag").get_attribute("href")
            prodata=json.dumps({'brand':brand,'name':product,'sp':sp, 'photo':image,'link':link})
            products.append(json.loads(prodata))
    driver.close()
    jsonoutput=json.dumps({'products':products})
    return json.loads(jsonoutput)
    
print(getTataCliq())