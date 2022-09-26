
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
        headers=False  # don`t generate misc headers
    )

    header=headers.generate()
    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=header)
    print(r.status_code)
    return e.extract(r.text)


def getAmazon(keyword):
    slug=slugify(keyword)
    link = 'https://www.amazon.in/s?k='+slug
    print(link)
    data = scrape(link)
    return data



