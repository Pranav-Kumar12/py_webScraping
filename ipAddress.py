import requests

ip= requests.get("https://api64.ipify.org?format=json")
print(ip.json())