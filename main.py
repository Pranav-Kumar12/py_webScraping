import requests

def fetchAndSaveToFile(url, path):
    data= requests.get(url)
    with open(path, "w", encoding= "utf-8") as f:
        f.write(data.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetchAndSaveToFile(url, "data/toi_delhi.html")