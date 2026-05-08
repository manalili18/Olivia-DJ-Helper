#!/bin/env python3

"""
discogs.py

this file just interacts with the discogs api
rate limit is 25 per min for unauthorized
"""

import requests

from api_keys import headers, discogs_url



search_example=discogs_url+'database/search?release_title=nevermind&artist=nirvana&per_page=3&page=1'

response = requests.get(search_example,headers=headers)
print(response.json())




