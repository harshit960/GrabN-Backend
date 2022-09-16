from email import header
from selectorlib import Extractor
import requests 
import re
from fake_headers import Headers as fakehead




def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[^\w\s-]', '', s)
  s = re.sub(r'[\s_-]+', '-', s)
  s = re.sub(r'^-+|-+$', '', s)
  return s

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('search_results.yml')

def scrape(url):  
    headers = fakehead(
        # generate any browser & os headeers
        headers=True  # don`t generate misc headers
    )

    header=headers.generate()
    print(header)
    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=header)
    
    return e.extract(r.text)


def getSearchdata(keyword):
    slug=slugify(keyword)
    link = 'https://www.flipkart.com/search?q='+slug
    print(link)
    data = scrape(link)
    return data


