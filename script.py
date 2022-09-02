import wget
import webbrowser
import requests
import os;
from bs4 import BeautifulSoup

headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
        }

URL = "https://download.kbits.build.lab126.a2z.com/build_files/download/raspite_fireos_ship_8312/Nightly/1143/user/release-raspite-RS8312_user_1143.tgz"

#response = wget.download(URL, "instagram.tgz")

kbits_URL="https://kbits.build.lab126.a2z.com/?build_variant=Nightly&product=Ship_8312&product_family=FireOS8&project=raspite_fireos_ship_8312&status=success"

#webbrowser.open(kbits_URL)

def scrapper(kbits_URL):
    page = requests.get(kbits_URL, headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')
    print(soup)

scrapper(kbits_URL)