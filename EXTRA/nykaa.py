
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time 

def getajio():
    products=[]
    jsonoutput={}
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    option = webdriver.ChromeOptions()
    #option.add_argument('--headless')
    #option.add_argument('--start-maximized')
    #option.add_argument('--start-fullscreen')
    option.add_argument(f'user-agent={user_agent}')
    option.add_argument("--ignore-certificate-error")
    option.add_argument("--ignore-ssl-errors")
    option.add_argument('--single-process')
    #option.add_argument('--disable-dev-shm-usage')
    option.add_argument("--incognito")
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument("disable-infobars")
    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.nykaafashion.com/catalogsearch/result/?q=puma+tshirt&searchType=Manual&internalSearchTerm=puma+tshirt&p=6")
    time.sleep(5)
    for i in driver.find_elements(By.CLASS_NAME,"prod-ctr"):
        items =i.find_elements(By.CLASS_NAME,"plp-prod")
        for item in items:
            imageraw=item.find_elements(By.CLASS_NAME, "css-elhs5v")
            if len(imageraw) == 0:
                break
            else:
                image=imageraw[0].get_attribute('src')
            brand=item.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/section/article/div/div[1]/div[1]/a[1]/div/div[1]").text
            product=item.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/section/article/div/div[1]/div[1]/a[1]/div/div[2]").text
            sp=item.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/section/article/div/div[1]/div[1]/a[1]/div/div[3]/span[1]").text
            originalp=item.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/section/article/div/div[1]/div[1]/a[1]/div/div[3]/span[2]").text
            
            link=item.find_element(By.XPATH, "//*[@id='app']/div/div[1]/div/div/section/article/div/div[1]/div[1]/a[1]").get_attribute("href")
            prodata=json.dumps({'brand':brand,'name':product,'sp':sp, 'photo':image,'link':link})
            products.append(json.loads(prodata))
        driver.close()
    jsonoutput=json.dumps({'products':products})
    return json.loads(jsonoutput)
    
print(getajio())
