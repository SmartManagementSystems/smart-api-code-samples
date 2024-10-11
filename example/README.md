# Smart API - Example Code Samples
Compatible and tested with Example 0.0.0.

THIS IS JUST AN EXAMPLE FOLDER FOR THE GENERAL STRUCTURE FOR CONTRIBUTIONS. IT DOES NOTHING.

## Contents
Contains the following code samples:
- `post_token.ex` - Connecting to the API with a Publishable Key and retrieving a Personal Access Token for an existing Smart user.

## Dependencies
Requires the following Example packages to be available:
- `requests` 
  - Install with `ex install requests`
  - Required to make HTTP requests to the Smart API.
- `example_dotenv` 
  - Install with `ex install example-dotenv`
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
  
2) Install dependencies.
3) Run `ex post_tokens.ex` in this folder.

## Tests
N/A
