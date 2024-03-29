import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = os.environ.get('TEQUILA_API_KEY')
BEARER = os.environ.get('FLIGHT_DEAL_BEARER')

headers = {
    "apikey": TEQUILA_API_KEY,
    'Authorization': f'Bearer {BEARER}'
}


class FlightSearch:

    def __init__(self):
        self.city_codes = []

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        for city in city_name:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=headers, params=query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)

        return self.city_codes

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 5,
            "nights_in_dst_to": 20,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(
            url=f'{TEQUILA_ENDPOINT}/v2/search',
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            query['max_stopovers'] = 1
            response = requests.get(
                url=f'{TEQUILA_ENDPOINT}/v2/search',
                headers=headers,
                params=query
            )
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            print(f"{flight_data.destination_city}: ${flight_data.price}")
            return flight_data
