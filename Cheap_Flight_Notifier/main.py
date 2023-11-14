from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'DEN'

data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()

print('Welcome to Davis\' Flight Club')
print('We find the best flight deals and email you.')
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')

email = 'email1'
confirm_email = 'email2'

while email != confirm_email:
    email = input('What is your email?\n')
    confirm_email = input('Type your email again.\n')

print('You\'re in the club!')
data_manager.post_new_data(first_name, last_name, email)


sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    city_names = [row['city'] for row in sheet_data]
    data_manager.city_codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_codes()
    sheet_data = data_manager.get_destination_data()

destinations = {
    data['iataCode']: {
        'id': data['id'],
        'city': data['city'],
        'price': data['lowestPrice']
    } for data in sheet_data
}

tomorrow = datetime.now() + timedelta(days=1)
ten_month_from_now = datetime.now() + timedelta(days=(10 * 30))

for destination_code in destinations:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination_code,
        from_time=tomorrow,
        to_time=ten_month_from_now
    )
    print(flight.price)
    if flight is None:
        continue

    if flight.price < destinations[destination_code]["price"]:

        users = data_manager.get_customer_emails()
        print(users)
        emails = [row["email"] for row in users if 'email' in row]
        names = [row["firstName"] for row in users if 'firstName' in row]

        message = f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_emails(emails, message)
