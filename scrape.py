import json
import requests
import time

# Get a list of image url from a supplied subreddit and category 
def get_img(str1, str2):
    # Big number for major shenanigans 
    number = 99999
    url = "https://www.reddit.com/r/{}/{}/".format(str1,str2)
    # Request to fetch .json data
    r = requests.get("{}.json?limit={}".format(url, number), headers = {'user-agent': 'Mozilla/5.0'})
    
    # List to store urls and the following one to validate file format
    img_list = []
    formats = ["jpeg", "jpg", "png"]
    
    # Loop through all url and validate against permitted formats
    for post in r.json()['data']['children']:
        
        if ([ele for ele in formats if(ele in post['data']['url'])]):
            img_list.append(post['data']['url'])
    
    # Return the list of image urls
    return (img_list)



