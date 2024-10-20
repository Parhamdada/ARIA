import requests

# Your API key from IEEE Xplore
API_KEY = 'blahblahblah'

# Base URL for IEEE Xplore API
BASE_URL = 'http://ieeexploreapi.ieee.org/api/v1/search/articles'

# Example search query parameters
query_params = {
    'apikey': API_KEY,
    'format': 'json',
    'querytext': 'PLL',
    'max_records': 5,     # Limit the number of results
    'start_record': 1      # Start from the first record
}

# Making the request
response = requests.get(BASE_URL, params=query_params)

if response.status_code == 200:
    data = response.json()  # Parse the JSON data
    print("Results:")
    for article in data.get('articles', []):
        print(f"Title: {article.get('title')}")
        print(f"Authors: {article.get('authors')}")
        print(f"DOI: {article.get('doi')}")
        print("-----")
else:
    print(f"Failed to retrieve data: {response.status_code}")
