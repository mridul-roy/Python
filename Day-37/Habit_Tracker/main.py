import requests
from datetime import datetime

TOKEN = "cnjfonksdjpnvbvmnl"
USER_NAME = "arnob"
GRAPH_ID = "graph1"
pixela_endpoint = " https://pixe.la/v1/users"

# User_Creation
user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "Succeed, Thank you",

}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

# Graph_Creation
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "CodingTimeTracker",
    "unit": "min",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)


# Graph_value_creation
graph_value_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()
DATE = today.strftime("%Y%m%d")

value_config = {
    "date": DATE,
    "quantity": input("How many time you spend in coding practice?"),
}

graph_value_response = requests.post(url=graph_value_endpoint, json=value_config, headers=headers)
print(graph_value_response.text)

# Update_value
update_value_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"
updated_data = {
    "quantity": "00",
}

# updated_value_response = requests.put(url=update_value_endpoint, json=updated_data, headers=headers,)
# print(updated_value_response.text)

# Delete_value
delete_value_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{DATE}"

# delete_value_response = requests.delete(url=delete_value_endpoint, headers=headers)
# print(delete_value_response.text)
