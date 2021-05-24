import requests
import json
from datetime import datetime

NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRI_API_ID = '286f637e' 
NUTRI_API_KEY = 'e4a9040c237ff803e3801fabdced53bc'
GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 21

nutri_parameters = {
    "query": 'ran 3 miles and lifted 30 kg',
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    'x-app-id' : NUTRI_API_ID,
    'x-app-key' : NUTRI_API_KEY
}

response = requests.post(url = NUTRI_ENDPOINT, json=nutri_parameters, headers=header)
excersise_data = response.json()

SHEET_ENDPOINT = "https://api.sheety.co/330f5970bccae1a13ed97189c2226490/excersiseTracker/sheet1"


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in excersise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": excersise_data["name"].title(),
            "duration": excersise_data["duration_min"],
            "calories": excersise_data["nf_calories"]
        }
    }
    #No Auth
    sheet_response = requests.post(sheet_endpoint,json=sheet_inputs)
    #Basic Auth
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        auth=(
            'kartik', 
            'adqa36qwgdq3t3',
        )
    )
    #Bearer Token
    bearer_headers = {
    "Authorization": f"Bearer 'ttfsfdv34sdfsffwea43'"
    }
    sheet_response = requests.post(
        sheet_endpoint, 
        json=sheet_inputs, 
        headers=bearer_headers
    )
    print(sheet_response.text)
