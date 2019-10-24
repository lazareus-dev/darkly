import requests
import sys
from bs4 import BeautifulSoup
def read_url(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    files = (soup.find_all('a'))
    for f in files:
        file_name = f.extract().get_text()
        url_new = url + file_name
        url_new = url_new.replace(" ","%20")
        if(file_name[-1]=='/' and file_name !='../'):
            read_url(url_new)
        if(file_name=='README'):
            content = requests.get(url + 'README').text
            if 'aide' not in content and 'Demande' not in content and 'craquer' not in content and 'Non' not in content:
                print(content)
                sys.exit()

read_url("http://192.1.1.3/.hidden/")
