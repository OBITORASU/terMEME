import json
import requests
import time


def get_meme(str1, str2):
    number = 99999
    url = "https://www.reddit.com/r/{}/{}/".format(str1,str2)
    r = requests.get("{}.json?limit={}".format(url, number), headers = {'user-agent': 'Mozilla/5.0'})
    
    meme_list = []
    formats = ["jpeg", "jpg", "png"]
    
    for post in r.json()['data']['children']:
        
        if ([ele for ele in formats if(ele in post['data']['url'])]):
            meme_list.append(post['data']['url'])

    return (meme_list)



