import requests
import json

# response = requests.get("http://api.open-notify.org/astros.json")
# print()
# print("===== STATUS CODE =====")
# print(response.status_code)
# print()
# print("===== FORMATTED JSON DATA =====")
#
# # create a formatted string of the Python JSON object
# def jprint(obj):
#     text = json.dumps(obj, sort_keys=True, indent=4)
#     print(text)
#
# jprint(response.json())

# params = {
#     'filter_by': 'region=Sub-Saharan Africa',
#     'limit': 5
# }
#
# response = requests.get(
#     "https://api-server.dataquest.io/economic_data/countries",
#     params=params
# )
# data = json.loads(response.json())
# print(f"Total countries: {len(data)}")
# print(f"First country: {data[0]['short_name']}")

# JSONPlaceholder is a free API for testing
url = "https://jsonplaceholder.typicode.com/posts"

# The data we want to send
new_post = {
    'title': 'Learning Python APIs',
    'body': 'POST requests let you send data to APIs',
    'userId': 1
}

# Send the POST request
response = requests.post(url, json=new_post)

# Check if it worked
if response.status_code == 201:
    print("Post created successfully!")
    print(response.json())
else:
    print(f"Something went wrong: {response.status_code}")


