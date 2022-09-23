import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json

def getMeesho(keyword):
    products=[]
    jsonoutput={}
    user_agent ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    option = webdriver.ChromeOptions()
    option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    option.add_argument("--headless")
    option.add_argument("--disable-dev-shm-usage")
    option.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=option)
    option.headless=True
    #option.add_argument('--headless')
    #option.add_argument(f'user-agent={user_agent}')
    #option.add_argument("--ignore-certificate-error")
    #option.add_argument("--ignore-ssl-errors")
    #PATH ="C:\Program Files (x86)\chromedriver.exe"
    #driver = webdriver.Chrome(PATH,options=option)
    driver.get("https://www.meesho.com/search?q="+keyword+"&searchType=autosuggest&searchIdentifier=text_search")
    
    items =driver.find_elements(By.CLASS_NAME,"ProductList__GridCol-sc-8lnc8o-0")
    for item in items:
        imageraw=item.find_elements(By.CSS_SELECTOR, "a > div > div.NewProductCardstyled__ProductImage-sc-6y2tys-18.kiiIIO > picture > img")
        if len(imageraw) == 0:
            break
        else:
            image=imageraw[0].get_attribute('src')
        brand=item.find_element(By.CLASS_NAME, "NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5").text
        product=item.find_element(By.CLASS_NAME, "NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5").text
        sp=item.find_element(By.CLASS_NAME, "BBZyK").text
        #originalp=item.find_element(By.CLASS_NAME, "gKNxow").text
        
        link=item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        prodata=json.dumps({'productBrand':brand,'title':product,'flipkartSpecialPrice':sp, 'imageUrls':image,'productUrl':link,'store':'meesho'})
        products.append(json.loads(prodata))
    driver.close()
    jsonoutput=json.dumps({'products':products})
    return json.loads(jsonoutput)
    
