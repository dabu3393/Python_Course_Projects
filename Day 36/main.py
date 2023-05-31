import requests
import os
from twilio.rest import Client

STOCK = "MA"
COMPANY_NAME = "Mastercard Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TWILIO_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
PERSONAL_CELL = os.environ.get('PERSONAL_CELL')

news_parameters = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME,
}

stock_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_data = stock_response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]

yesterday_price = data_list[0]['4. close']
day_before_yesterday_price = data_list[1]['4. close']

closing_diff = float(yesterday_price) - float(day_before_yesterday_price)
up_down = None
if closing_diff > 0:
    up_down = '🔺'
else:
    up_down = '🔻'
print(closing_diff)

diff_percent = round((closing_diff/float(yesterday_price))*100, 2)
print(diff_percent)

if abs(diff_percent) >= 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()['articles']
    three_articles = articles[:3]

    formatted_articles = [f"{COMPANY_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+18666983577',
            to=PERSONAL_CELL
        )
        print(message.status)