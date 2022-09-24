from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import os
import time
def getMynta(keyword):
    products=[]
    jsonoutput={}
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    option = webdriver.ChromeOptions()
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    #option.add_argument("--headless")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    option.add_argument(f'user-agent={user_agent}')
    #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=option)
    #option.headless=True
    #option.add_argument('--headless')
    #option.add_argument(f'user-agent={user_agent}')
    #option.add_argument("--ignore-certificate-error")
    #option.add_argument("--ignore-ssl-errors")
    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.myntra.com/"+keyword)
    driver.execute_script("window.scrollBy(0,4000)","")
    time.sleep(2)
    items =driver.find_elements(By.CLASS_NAME,"product-base")
    for item in items:
        imageraw=item.find_elements(By.CSS_SELECTOR, "picture > img")
        if len(imageraw) == 0:
            print(imageraw)
            break
        else:
            image=imageraw[0].get_attribute('src')
            #print(image)
        brand=item.find_element(By.CLASS_NAME, "product-brand").text
        product=item.find_element(By.CLASS_NAME, "product-product").text
        sp=item.find_element(By.XPATH, "//*[@id='desktopSearchResults']/div[2]/section/ul/li[7]/a/div[2]/div/span[1]/span[1]").text
        originalp=item.find_element(By.XPATH, "//*[@id='desktopSearchResults']/div[2]/section/ul/li[7]/a/div[2]/div/span[1]/span[2]").text
        rating=item.find_element(By.XPATH,"//*[@id='desktopSearchResults']/div[2]/section/ul/li[4]/div[2]/span[1]").text
        rated_by=item.find_element(By.XPATH,"//*[@id='desktopSearchResults']/div[2]/section/ul/li[4]/div[2]/div").text
        link=item.find_element(By.XPATH, "//*[@id='desktopSearchResults']/div[2]/section/ul/li[1]/a").get_attribute("href")
        prodata=json.dumps({'productBrand':brand,'title':product,'flipkartSpecialPrice':sp,'flipkartSellingPrice':originalp, 'imageUrls':image,'productUrl':link,'Rating':rating,'Rated_by':rated_by,'store':'Myntra'})
        products.append(json.loads(prodata))
    driver.close()
    jsonoutput=json.dumps({'products':len(products)})
    return json.loads(jsonoutput)
print(getMynta('tshirt'))