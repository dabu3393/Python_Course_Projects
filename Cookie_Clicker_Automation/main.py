from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url = 'https://orteil.dashnet.org/experiments/cookie/'
chrome_driver_path = '/Users/davisburrill/Development/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(url)

cookie = driver.find_element(By.ID, 'cookie')

items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5

while True:

    cookie.click()

    cookie_per_sec_element = driver.find_element(By.ID, 'cps').text
    cookie_per_sec = float(cookie_per_sec_element.split(':')[1].strip())

    if time.time() > timeout:

        all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = [int(price.text.split('-')[1].strip().replace(',', '')) for price in all_prices if price.text != '']

        print(item_prices)
        cookie_store = {}
        for n in range(len(item_prices)):
            cookie_store[item_prices[n]] = item_ids[n]

        count = driver.find_element(By.ID, 'money').text
        if ',' in count:
            count = count.replace(',', '')
        cookie_count = int(count)

        affordable_upgrades = {cost: item_id for cost, item_id in cookie_store.items() if cookie_count > cost}

        highest_price_affordable = max(affordable_upgrades)
        purchase_id = affordable_upgrades[highest_price_affordable]

        purchase_button = driver.find_element(By.ID, purchase_id)
        purchase_button.click()

        timeout = time.time() + 5

    if cookie_per_sec > 300:
        break
