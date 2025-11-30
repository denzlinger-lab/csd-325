import requests
import json

try:
    response = requests.get("http://api.open-notifi.org/iss-now.json", timeout=5)
    response.raise_for_status()
    data = response.json()
    print(response.status_code)
    # print(f"ISS Location: {data}")
except requests.exceptions.Timeout:
    print("The request timed out. The server took too long to respond.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred:{e}")
except requests.exceptions.RequestException as e:
    print(f"Something went wrong: {e}")

# try:
#     response = requests.get("https://anapioficeandfire.com/api/houses", timeout=5)
#     response.raise_for_status()
#     data = response.json()
#     print(response.status_code)
# except requests.exceptions.Timeout:
#     print("The request timed out. The server took too long to respond.")
# except requests.exceptions.HTTPError as e:
#     print(print(f"HTTP error occurred: {e}"))
# except requests.exceptions.RequestException as e:
#     print(f"Something went wrong: {e}")