
import requests

# url = "https://kitchen-api-hebwau5dkq-ew.a.run.app"
url = "http://0.0.0.0:8000"

params = { "ingredients": "chicken,potato,spinach"
          , "preferences": "dinner,easy" }

res = requests.get(url + "/predict", params=params)

# res = requests.get(url + "/")

print(res.content)
