import json
from urllib import response

import requests


def get_quote():
    URL = "https://api.quotable.io/random"
    try:
        response = requests.get(URL)
    except:
        print("Error while calling the API...")


res = json.loads(response.text)
print(res['content'] + "-" + res['author'])