import json
import requests
import time



def get_meme(str):
    number = 99999
    url = "https://www.reddit.com/r/dankmemes/{}/".format(str)
    r = requests.get("{}.json?limit={}".format(url, number), headers = {'user-agent': 'Mozilla/5.0'})
    
    meme_list = []

    for post in r.json()['data']['children']:
        if "gif" not in post['data']['url']:
            meme_list.append(post['data']['url'])

    return (meme_list)





