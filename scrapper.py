import urllib.request
import time

def download_site(url):
        with urllib.request.urlopen(url) as response:
            print (f"Stiahnutie {url}: {len(response.read())} bytov")


sites = [
    "http://www.autino.sk",
    "http://www.yahoo.com",
    "http://www.google.com",
]

start_time = time.time()
for site in sites:
    download_site(site)

duration = time.time() - start_time
print(f"Stiahnute {len(sites)} stranok za {duration} sekund")