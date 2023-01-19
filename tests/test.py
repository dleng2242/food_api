import requests

# BASE = "http://127.0.0.1:5000"
# BASE = "http://127.0.0.1:7071"
BASE = "https://duncans-food-api.azurewebsites.net"

# check basic usage - returns two soups
response = requests.get(BASE + "/food/soup/2")
print(response.json())

# check it returns all the soups
response = requests.get(BASE + "/food/soup/0")
print(response.json())

# check the default returns just one soup
response = requests.get(BASE + "/food/soup")
print(response.json())

response = requests.get(BASE + "/food/pasta")
print(response.json())

response = requests.get(BASE + "/food/notfound")
print(response.json())

response = requests.get(BASE + "/food/stew/0")
print(response.json())

response = requests.put(BASE + "/food/stew", data={"food_item": "delicious stew"})
print(response.json())

response = requests.get(BASE + "/food/stew/0")
print(response.json())

response = requests.put(BASE + "/food/stew", data={"food_item": "lentil stew"})
print(response.json())

# add to pasta by mistake
response = requests.put(BASE + "/food/pasta", data={"food_item": "lentil stew"})
print(response.json())

# check its there
response = requests.get(BASE + "/food/pasta/0")
print(response.json())

# remove it
response = requests.delete(BASE + "/food/pasta", data={"food_item": "lentil stew"})
print("Deleted: ", response, response.status_code)

# check its gone
response = requests.get(BASE + "/food/pasta/0")
print(response.json())
