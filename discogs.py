#!/usr/bin/env python3

"""
discogs.py

this file just interacts with the discogs api
rate limit is 25 per min for unauthorized

take in the input.csv 
output json with all pertintent info

"""

import requests, csv, time, json, datetime

from api_keys import headers, discogs_url

hourmin_now=datetime.datetime.now().strftime('%H%M')

output_csv='output.discogs.'+hourmin_now+'.csv'
err_txt='errors.'+hourmin_now+'.txt'

with open('input.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        album=row['album']
        artist=row['artist']
        # year=row['year']

        # search_str='https://api.discogs.com/database/search?release_title='+album+'&artist='+artist+'&year='+year+'&format=Vinyl&per_page=1&page=1'
        search_str='https://api.discogs.com/database/search?release_title='+album+'&artist='+artist+'&format=Vinyl&per_page=1&page=1'

        # print(search_str)

        print('searching for',album,'-',artist,'...')
        response = requests.get(search_str,headers=headers)
        # print(response.json())
        search_dict=response.json()

        # init vars
        # TODO: id may not be universally albums
        
        id_str=''
        tracklist=''
        genres=''
        styles=''


        try:
            id_str = str(search_dict["results"][0]["id"])
        except IndexError:
            with open(err_txt,'a') as error_f:
                error_f.write(album+artist+':maybe no results:')
                error_f.write(search_str)
                error_f.write('\n')
            print('aww rats!')

        
        # print(id)

        print('retrieving tracks for',album,'-',artist,'...')
        release_str='https://api.discogs.com/releases/'+id_str

        response = requests.get(release_str,headers=headers)
        try:
            release_dict=response.json()
        except json.decoder.JSONDecodeError:
            print('aww rats!')
            with open(err_txt,'a') as error_f:
                error_f.write(album+artist+':json fail:')
                error_f.write(release_str)
                error_f.write('\n')

        try:
            tracklist=release_dict['tracklist']
        except KeyError:
            print('aww rats!')
            with open(err_txt,'a') as error_f:
                error_f.write(album+artist+':tracklist fail:')
                error_f.write(release_str)
                error_f.write('\n')

        try:
            genres=release_dict['genres']
        except KeyError:
            print('aww rats!')
            with open(err_txt,'a') as error_f:
                error_f.write(album+artist+':genres fail:')
                error_f.write(release_str)
                error_f.write('\n')

        try:
            styles=release_dict['styles']
        except KeyError:
            print('aww rats!')
            with open(err_txt,'a') as error_f:
                error_f.write(release_str)
                error_f.write('\n')

        # print(genres,styles) 

        for track in tracklist:
            with open(output_csv,'a') as out_f:
                position=track['position']
                title=track['title']
                duration=track['duration']

                gensty = ','.join(genres+styles)

                # artist, track, album, position, other attributes
                seq = map(str,[artist,title,album,position,duration,gensty,search_str,release_str])

                out_str = ';'.join(seq)
                out_f.write(out_str)
                out_f.write('\n')

        time.sleep(5)
