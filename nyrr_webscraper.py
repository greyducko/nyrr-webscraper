# Author: Harvey Ng
# Description: Web scraper that searches the New York Road Runners' website for "9+1" volunteer
# opportunities. Uses the Selenium Webdriver to navigate the website through the Firefox browser.
# The opportunities are saved into a data.json file.

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import json


# Open Firefox and go to NYRR volunteer opportunities page
browser = webdriver.Firefox()
browser.get("https://www.nyrr.org/getinvolved/volunteer/opportunities?available_only=true&itemId"
            "=3EB6F0CC-0D76-4BAF-A894-E2AB244CEB44&limit=8&offset=0&opportunity_type=9%2B1%20Quali"
            "fier&totalItemLoaded=8")

# Accept cookies by clicking (sometimes this blocks the ability to click "LOAD MORE" button)

cookies = browser.find_element(By.LINK_TEXT, "ACCEPT")
cookies.click()

# Find "LOAD MORE" button
loadMore = browser.find_element(By.LINK_TEXT, "LOAD MORE")

# Keep pressing the "LOAD MORE" button until the entire page of opportunities is loaded
while loadMore.is_displayed():
    try:
        # if there is no more "LOAD MORE" button, a no such element exception is raised
        loadMore = browser.find_element(By.LINK_TEXT, "LOAD MORE")
        loadMore.click()
    except selenium.common.exceptions.NoSuchElementException:
        break
    except selenium.common.exceptions.ElementNotInteractableException:
        break

# Locate the elements that fit the following class names
title = browser.find_elements(By.CLASS_NAME, "role_listing__title")
event = browser.find_elements(By.CLASS_NAME, "role_listing__event")
desc = browser.find_elements(By.CLASS_NAME, "role_listing__desc")
date = browser.find_elements(By.CLASS_NAME, "role_listing__date")
time = browser.find_elements(By.CLASS_NAME, "role_listing__time")
location = browser.find_elements(By.CLASS_NAME, "role_listing__location")

# Save the opportunities as a list of dictionaries
length = len(title)
list_of_events = []
for i in range(length):
    dict_event = {
        "title": title[i].text,
        "event": event[i].text,
        "description": desc[i].text,
        "date": date[i].text,
        "time": time[i].text,
        "location": location[i].text
    }
    list_of_events.append(dict_event)

# Save the volunteer opportunities into a json file
with open("data.json", "w") as f:
    json.dump(list_of_events, f)



