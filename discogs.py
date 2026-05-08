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
        # print(row['album'], row['artist'])
        # this search string works yay keeeeeep it
        # search_str='https://api.discogs.com/database/search?release_title=' +row['album'] +'&artist=' +row['artist'] +'&per_page=1&page=1'
        search_str='https://api.discogs.com/database/search?release_title=' +row['album'] +'&artist=' +row['artist'] +'&format=Vinyl&per_page=1&page=1'

        # print(search_str)

        response = requests.get(search_str,headers=headers)
        # print(response.json())
        search_dict=response.json()

        id = str(search_dict["results"][0]["id"])
        print(id)

        release_str='https://api.discogs.com/releases/'+id

        response = requests.get(release_str,headers=headers)
        release_dict=response.json()
        tracklist=release_dict['tracklist']
        genres=release_dict['genres']
        styles=release_dict['styles']
        print(genres,styles) 
        for track in tracklist:
            print(track['position'])
            print(track['title'])
            print(track['duration'])
# search_example=discogs_url+'database/search?release_title=nevermind&artist=nirvana&per_page=3&page=1'
# 
# response = requests.get(search_example,headers=headers)
# print(response.json())




