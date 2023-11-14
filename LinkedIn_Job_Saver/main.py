from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3513143965&f_AL=true&f_E=1%2C2&geoId=103736294&keywords=junior%20python%20developer&location=Denver%2C%20Colorado%2C%20United%20States&refresh=true&sortBy=R'

chrome_driver_path = '/Users/davisburrill/Development/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
action = ActionChains(driver)

driver.get(URL)

sign_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(5)

email_input = driver.find_element(By.ID, 'username')
email_input.send_keys(os.environ.get('LINKEDIN_USERNAME'))

password_input = driver.find_element(By.ID, 'password')
password_input.send_keys(os.environ.get('LINKEDIN_PASSWORD'))

sign_in_2 = driver.find_element(By.CSS_SELECTOR, '.login__form_action_container button')
sign_in_2.click()

time.sleep(10)

job_postings_section = driver.find_element(By.CSS_SELECTOR, '.scaffold-layout__list-container')
list_of_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in list_of_jobs:
    # Scroll to the job posting section to bring it into view
    driver.execute_script("arguments[0].scrollIntoView();", job_postings_section)
    time.sleep(0.5)  # Add a small delay for scrolling to complete

    # Scroll to the job posting to bring it into view within the section
    driver.execute_script("arguments[0].scrollIntoView();", job)
    time.sleep(0.5)  # Add a small delay for scrolling to complete

    # Click on the job posting
    job.click()
    time.sleep(2)  # Add a small delay after clicking to allow the page to load

    # Click on the "Save job" button
    save_button = driver.find_element(By.CSS_SELECTOR, '.mt5 .display-flex .jobs-save-button')
    save_button.click()
    time.sleep(1)  # Add a small delay after clicking the button

driver.quit()