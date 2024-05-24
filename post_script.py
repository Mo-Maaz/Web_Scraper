import requests
import time

# URL of the scraper service
SCRAPER_SERVICE_URL = "http://localhost:8080"

# Define the JSON payload to send in the POST request
payload = {"url": "http://google.com"}

# Interval between requests (in seconds)
interval = 30

while True:
    try:
        # Make an HTTP POST request to the scraper service
        response = requests.post(SCRAPER_SERVICE_URL, json=payload)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("Request successful:", response.text)
        else:
            print("Request failed with status code:", response.status_code)

    except Exception as e:
        print("Error:", e)

    # Wait for the specified interval before making the next request
    time.sleep(interval)
