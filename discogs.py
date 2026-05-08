#!/usr/bin/env python3

"""
discogs.py

this file just interacts with the discogs api
rate limit is 25 per min for unauthorized

take in the input.csv 
output track list with time length

"""

import requests, csv

from api_keys import headers, discogs_url


with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['album'], row['artist'])
        # this search string works yay keeeeeep it
        # search_str='https://api.discogs.com/database/search?release_title=' +row['album'] +'&artist=' +row['artist'] +'&per_page=1&page=1'
        search_str='https://api.discogs.com/database/search?release_title=' +row['album'] +'&artist=' +row['artist'] +'&per_page=1&page=1'

        print(search_str)

        response = requests.get(search_str,headers=headers)
        print(response.json())


# search_example=discogs_url+'database/search?release_title=nevermind&artist=nirvana&per_page=3&page=1'
# 
# response = requests.get(search_example,headers=headers)
# print(response.json())




