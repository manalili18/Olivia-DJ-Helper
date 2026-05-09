#!/usr/bin/env python3

"""
discogs.py

this file just interacts with the discogs api
rate limit is 25 per min for unauthorized

take in the input.csv 
output json with all pertintent info

"""

import requests, csv, time

from api_keys import headers, discogs_url


with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        album=row['album']
        artist=row['artist']
        year=row['year']

        # search_str='https://api.discogs.com/database/search?release_title='+album+'&artist='+artist+'&year='+year+'&format=Vinyl&per_page=1&page=1'
        search_str='https://api.discogs.com/database/search?release_title='+album+'&artist='+artist+'&format=Vinyl&per_page=1&page=1'

        # print(search_str)

        print('searching for',album,'-',artist,'...')
        response = requests.get(search_str,headers=headers)
        # print(response.json())
        search_dict=response.json()

        try:
            id = str(search_dict["results"][0]["id"])
        except IndexError:
            with open('errors.txt','a') as error_f:
                error_f.write(search_str)
                error_f.write('\n')

        
        # print(id)

        print('retrieving tracks for',album,'-',artist,'...')
        release_str='https://api.discogs.com/releases/'+id

        response = requests.get(release_str,headers=headers)
        try:
            release_dict=response.json()
            tracklist=release_dict['tracklist']
            genres=release_dict['genres']
            styles=release_dict['styles']
        except json.decoder.JSONDecodeError:
            error_f.write(release_str)
            error_f.write('\n')
        except KeyError:
            error_f.write(release_str)
            error_f.write('\n')

        # print(genres,styles) 

        for track in tracklist:
            continue
            print(track['position'])
            print(track['title'])
            print(track['duration'])
        time.sleep(5)
