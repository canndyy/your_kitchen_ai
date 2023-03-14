
import requests
url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"
res = requests.get(url + "/")


params = { "ingredients": "chicken,potato,spinach"
          , "preferences": "dinner,easy" }

res = requests.get(url + "/predict", params=params)

print(res.content)

# res = requests.get(url + "/")
# url = "http://0.0.0.0:8000"
