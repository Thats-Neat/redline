import json
from urllib.request import urlopen
import socket

def get_website_info(website):
    
    
    if website.startswith('https://'):
        website = website.removeprefix('https://')
        if not website.startswith('www.'):
            website = f'www.{website}.com'
        
    website = socket.gethostbyname(website)
    
    url = f'https://ipinfo.io/{website}/json'
    response = urlopen(url)
    data = json.load(response)

    ip = data["ip"]
    city = data["city"]
    region = data["region"]
    country = data["country"]
    location = data["loc"]
    postal = data["postal"]
    timezone = data["timezone"]
    
    return ip, city, region, country, location, postal, timezone
    