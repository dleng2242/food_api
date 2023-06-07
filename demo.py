import requests

# Update your base URL, e.g. "http://127.0.0.1:5000", or if deployed "https://<function>.azurewebsites.net"
BASE = "http://127.0.0.1:5000"

# check basic usage - returns two soups
response = requests.get(BASE + "/food/soup/2")
print(response.json())
input()

# check it returns all the soups
response = requests.get(BASE + "/food/soup/0")
print(response.json())
input()

# check the default returns just one soup
response = requests.get(BASE + "/food/soup")
print(response.json())
input()

response = requests.get(BASE + "/food/pasta")
print(response.json())
input()

response = requests.get(BASE + "/food/notfound")
print(response.json())
input()

response = requests.get(BASE + "/food/stew/0")
print(response.json())
input()

response = requests.put(BASE + "/food/stew", data={"food_item": "delicious stew"})
print(response.json())
input()

response = requests.get(BASE + "/food/stew/0")
print(response.json())
input()

response = requests.put(BASE + "/food/stew", data={"food_item": "lentil stew"})
print(response.json())
input()

# add to pasta by mistake
response = requests.put(BASE + "/food/pasta", data={"food_item": "lentil stew"})
print(response.json())
input()

# check its there
response = requests.get(BASE + "/food/pasta/0")
print(response.json())
input()

# remove it
response = requests.delete(BASE + "/food/pasta", data={"food_item": "lentil stew"})
print("Deleted: ", response, response.status_code)
input()

# check its gone
response = requests.get(BASE + "/food/pasta/0")
print(response.json())
