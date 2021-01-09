import json
import requests
import time


# A function to scrape memes from subreddits 
def get_meme(str1, str2):
    
    # A big number so you dont run out of dankness
    number = 99999
    # url to scrape from
    url = "https://www.reddit.com/r/{}/{}/".format(str1,str2)
    
    # Using requests module to scrape the .json data
    r = requests.get("{}.json?limit={}".format(url, number), headers = {'user-agent': 'Mozilla/5.0'})
    # An empty list to store all the shenanigans
    meme_list = []
    formats = ["jpeg", "jpg", "png"]
    # Loop through the list
    for post in r.json()['data']['children']:
        
        if([ele for ele in formats if(ele in post['data']['url'])]):
            # Get the url of the meme 
            meme_list.append(post['data']['url'])
    
    # Return the list populated list of meme url
    return (meme_list)





