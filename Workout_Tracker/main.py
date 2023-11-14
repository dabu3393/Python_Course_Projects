import requests
import os
from datetime import datetime

USERNAME = os.environ.get('PIXELA_USERNAME')
TOKEN = os.environ.get('PIXELA_TOKEN')
GRAPH_ID = 'workout1'

user_choice = input('What would you like to do?\n1. Add Pixel\n2. Update Pixel\n3. Delete Pixel\nPlease enter number: ')

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# # CREATES A USER WITH PIXELA
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id': GRAPH_ID,
    'name': 'Workout Graph',
    'unit': 'Hours',
    'type': 'float',
    'color': 'momiji',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# # CREATES YOUR GRAPH
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

update_graph_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

update_graph_config = {
    'unit': 'Hours',
    'timezone': 'America/Denver'
}

# # UPDATE YOUR GRAPH
# response = requests.put(url=update_graph_endpoint, json=update_graph_config, headers=headers)
# print(response.text)


# If you need to do previous days, datetime(year=<year>, month=<month>, day=<day>) should be used
today = datetime.now()

if user_choice == '1':
    post_pixel_endpoint = f'{graph_endpoint}/{GRAPH_ID}'

    post_pixel_config = {
        'date': today.strftime('%Y%m%d'),
        'quantity': input('How many hours did you workout today? '),
    }

    # POSTS A PIXEL WITH DATA FOR WHAT YOU ARE TRACKING
    response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
    print(response.text)


if user_choice == '2':
    update_date = input('What is the date of the pixel you want updated? (YYYYMMDD) ')
    update_endpoint = f'{graph_endpoint}/{GRAPH_ID}/{update_date}'
    new_pixel_data = {
        'quantity': input('How many hours did you want to put instead? ')
    }

    # UPDATES EXISTING PIXELS WITH NEW DATA
    response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
    print(response.text)

if user_choice == '3':
    delete_date = input('What is the date of the pixel you want deleted? (YYYYMMDD) ')
    delete_endpoint = f'{graph_endpoint}/{GRAPH_ID}/{delete_date}'

    # DELETES AN EXISTING PIXEL FROM YOUR GRAPH
    response = requests.delete(url=delete_endpoint, headers=headers)
    print(response.text)
