#!/usr/bin/env python3

"""
main.py
This is the main file for executing the DJ helper
"""

import requests

from api_keys import gsb_url, gsb_key

search_example=gsb_url+'search/?api_key='+gsb_key+'&type=artist&lookup=metallica'

print(search_example)

response = requests.get(search_example)
print(response.json())

