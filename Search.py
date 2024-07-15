import requests

url = "https://www.bing.com/search?q=吴青峰"

resp = requests.get(url)

print(resp)
print(resp.text)