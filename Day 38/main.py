import requests
from datetime import datetime
import os

APP_ID = os.environ.get('NUTRITIONIX_ID')
API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

GENDER = 'male'
WEIGHT_KG = 86
HEIGHT_CM = 187.96
AGE = 24

exercise_activities = input('Tell me what exercises you did: ')

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')

exercise_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'x-remote-user-id': '0',
}

exercise_params = {
    'query': exercise_activities,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_data = exercise_response.json()['exercises']

today_date = datetime.now().strftime('%d/%m/%Y')
today_time = datetime.now().strftime('%H:%M:%S')

sheety_headers = {
    'Authorization': f'Bearer {os.environ.get("SHEETY_BEARER_TOKEN")}'
}

for exercise in exercise_data:
    row_contents = {
        'workout': {
            'date': today_date,
            'time': today_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories'],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint, json=row_contents, headers=sheety_headers)
    print(sheety_response.text)




