import requests
import urllib.parse
from src import accounts


def token():

    url = "https://auth.1iu.ru/api/account/login"

    data_req = [("consumer", "at"),
                ("login", accounts.acc["radwexe"]["login"]),
                ("password", accounts.acc["radwexe"]["pass"])]

    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.109 Safari/537.36',
        'Referer': 'https://antitreningi.ru/',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers1, data=urllib.parse.urlencode(data_req))
    return response.json()['sid']


