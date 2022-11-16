import requests

url = "https://api.metadefender.com/v4/ip/34.214.215.3"

headers = {
    "apikey" : "c5285335ebf77b9a33142bdd0a0d5d9d"
}

respomse = requests.request("GET", url, headers=headers)

print(respomse.text)