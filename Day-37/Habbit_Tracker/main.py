import requests


pixela_endpoint = " https://pixe.la/v1/users"

user_param = {
    "token": "cnjfonksdjpnvbvmnl",
    "username": "arnob",
    "agreeTermsOfService": "yes",
    "notMinor" : "yes",
    "thanksCode" : "Succed, Thank you",

}

responce = requests.post(url=pixela_endpoint, json=user_param)
print(responce.text)