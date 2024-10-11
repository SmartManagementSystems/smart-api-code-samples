# Special thanks to Adonis Zhao from TVSA Pilot Training for starting this code.

import requests
import os
from dotenv import load_dotenv
 
# Load the environment variables from the .env file
load_dotenv()

TOKENS_URL = "https://api.smartaviation.net/v1/tokens"

# Replace with your App ID from the API Applications Manager
# Required headers for the POST request
headers = {
    "Accept": "application/json", # Standard required header
    "Content-Type": "application/json", # Standard required header
    "X-Application-Id": os.getenv('APP_ID'),
    "Authorization": "Bearer " + os.getenv('PUBLISHABLE_KEY'),
    "X-Tenant": os.getenv('TENANT_ID'),
}

# Data for the POST request - Replace with the correct fields expected by the API
data = {
    "email": os.getenv('USER_EMAIL'), # The Smart user's email address
    "password": os.getenv('USER_PASSWORD'), # The Smart user's password (plain-text)
    "two_factor_code": os.getenv('USER_2FA'), # If two-factor authentication is enabled for the user
    "device_name": "My Device", # An device name to identify the device that requested the token
}

# Make the POST request to the /tokens endpoint
response = requests.post(
    url = TOKENS_URL, 
    headers = headers, 
    json = data,
)

# Success (201 - Created) or failure (any other status code isn't what we expect)
if response.status_code == 201: 
    # Print the JSON data, which should include the token (if new token)
    print("Success! Token generated:")
    print(response. json()) 
else:
    # Print an error message
    print(f"Request failed with status code: {response.status_code}")
    print("Error response from the server:")
    print(response.text) 
