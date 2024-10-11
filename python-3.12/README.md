# Smart API - Python Code Samples
Compatible and tested with Python 3.12.

## Contents
Contains the following code samples:
- `post-tokens.py` - Connecting to the API with a Publishable Key and retrieving a Personal Access Token for an existing Smart user.

## Dependencies
Requires the following Python packages to be available:
- `requests` 
  - Install with `pip install requests`
  - Required to make HTTP requests to the Smart API.
- `python_dotenv` 
  - Install with `pip install python-dotenv`
  - Required to read the `.env` file in this folder containing secrets that should not be committed to source control.

## Basic Usage
1) Create and configure your `.env` file from following sample:
```
# API AUTHENTICATION
# Set your application ID from the API Applications Manager
APP_ID = ""

# Set your publishable key from the API Applications Manager
PUBLISHABLE_KEY = "" 

# Set your Tenant ID. This is case sensitive!
TENANT_ID = ""

# USER AUTHENTICATION
# The email address of the Smart user
USER_EMAIL = ""

# The password for the Smart user
USER_PASSWORD = ""

# The 2FA code for the Smart user
USER_2FA = ""
```
  
2) Install Python dependencies.
3) Run `python post-tokens.py` in this folder.

## Tests
N/A