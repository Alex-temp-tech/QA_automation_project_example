import requests
import urllib.parse
from src import accounts
from configuration import Configuration


def token():

    url = Configuration.base_url_for_token

    data_req = [("consumer", "at"),
                ("login", accounts.acc[Configuration.acc_for_test]["login"]),
                ("password", accounts.acc[Configuration.acc_for_test]["pass"])]

    headers1 = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.109 Safari/537.36',
        'Referer': Configuration.base_url,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers1, data=urllib.parse.urlencode(data_req))
    return "/account/auth?&token=" + response.json()['sid']
