import requests 
from pprint import pprint

url = requests.get("https://api.ipify.org/?format=json")
loc = requests.get("https://ipinfo.io/")

pprint(url.text)
pprint(loc.text)
