
import requests
url = "http://0.0.0.0:8080"
res = requests.get(url + "/")

print(res.content)
