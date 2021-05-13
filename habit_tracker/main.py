'''website : https://pixe.la/v1/users/nyuboy/graphs/graph1.html'''

import requests
import json
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'nyuboy'
TOKEN = "dsad765asdsd8as32sda"

user_parameters = {
    'token' : TOKEN,
    'username' : USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',
}

# response = requests.post(url = ENDPOINT, json = user_parameters)
# print(response.text)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = 'graph1'

graph_parameters = {
    'id' : GRAPH_ID,
    'name' : 'Coding Graph',
    'unit' : 'minutes',
    'type' : 'int',
    'color' : 'shibafu',
}

header = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url = GRAPH_ENDPOINT, json = graph_parameters, headers = header)
# print(response.text)

POST_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

DATE = datetime(year = 2021, month = 5, day = 12)

post_parameters = {
    'date' : DATE.strftime("%Y%m%d"),
    'quantity' : input('How many minutes did U code: '),
}

response = requests.post(url = POST_ENDPOINT, json = post_parameters, headers = header)
print(response.text)

'''Update'''
PUT_ENDPOINT = f"{POST_ENDPOINT}/{DATE.strftime('%Y%m%d')}"

put_parameters = {
    'quantity' : '150',
}

# response = requests.put(url = PUT_ENDPOINT, json = put_parameters, headers = header)
# print(response.text)

'''DELETE'''
DELETE_ENDPOINT = f"{POST_ENDPOINT}/{DATE.strftime('%Y%m%d')}"

# response = requests.delete(url = DELETE_ENDPOINT, headers = header)
# print(response.text)