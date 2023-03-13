
import requests
url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"
res = requests.get(url + "/")

print(res.content)
