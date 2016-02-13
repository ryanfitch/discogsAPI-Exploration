#simple python program using the discogs client api for an artist / album search query

import discogs_client
import requests
import json
import webbrowser

d = discogs_client.Client('ryanApplication/0.1', user_token='KANMCufpThOrsRsbbudaArVQlhRFpqtVWyqsIlfD')
dToken = 'KANMCufpThOrsRsbbudaArVQlhRFpqtVWyqsIlfD'

def albumSearch (albumName, artistName):
    results = d.search(albumName, artist=artistName, type='release')
    print("-=-=-=-=-=-=-=-=-=-")
    print("There are {} items found.".format(results.count))
    for item in results.page(1):
        print(item)

def moreInfo (releaseNum):
    r = requests.get('https://api.discogs.com/database/search?q='+releaseNum+'&token=' + dToken)
    fullInfo = r.json()
    for info in fullInfo['results']:
        url = "http://discogs.com" + info['uri']
        webbrowser.open_new(url)
        
artistName = str(input("Please give me a name of an artist you want to search: "))
albumName = str(input("Please give me a name of an album by that artist you want to search: "))
albumSearch(albumName, artistName)

releaseNum = input("Please give me the release number you would like more information about: ")
moreInfo(releaseNum)
