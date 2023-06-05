from pprint import pprint
import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ.get('FLIGHT_DEAL_SHEETY_PRICES_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.environ.get('FLIGHT_DEAL_SHEETY_USERS_ENDPOINT')

BEARER = os.environ.get('FLIGHT_DEAL_BEARER')

headers = {
    'Authorization': f'Bearer {BEARER}'
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        pprint(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data

    def post_new_data(self, first_name, last_name, email):

        new_data = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }

        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=new_data, headers=headers)
        response.raise_for_status()
        print(response.text)