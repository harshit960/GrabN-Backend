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


    # Download the page using requests
    print("Downloading %s"%url)
    r = requests.get(url, headers=headers.generate())
    # Simple check to check if page was blocked (Usually 503)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
        else:
            print("Page %s must have been blocked by Amazon as the status code was %d"%(url,r.status_code))
        return None
    # Pass the HTML of the page and create 
    return e.extract(r.text)


def getSearchdata(keyword):
    slug=slugify(keyword)
    link = 'https://www.amazon.in/s?k='+slug
    print(link)
    data = scrape(link)
    return data


