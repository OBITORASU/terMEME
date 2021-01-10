import json
import requests
import random

from clint.textui import colored
from urllib.request import urlopen, URLError

def check_validity():
    while True:
        reddit = input(colored.green("Enter the name of a valid subreddit: "))
        print(colored.green("\n[+] Checking subreddit validity....\n"))
        try:
            if not reddit.isspace():
                urlopen("https://www.reddit.com/r/{}".format(reddit))
                print(colored.green("\n[+] Subreddit found!\n"))
                break
            else:
                print(colored.red("[-] Invalid subreddit"))
        except URLError:
            print(colored.red("[-] Invalid subreddit!"))

    return reddit



# Get a list of image url from a supplied subreddit and category 
def get_content(reddit, category):

    # Big number for major shenanigans 
    url = "https://www.reddit.com/r/{}/{}/".format(reddit,category)
    # Request to fetch .json data
    r = requests.get("{}.json?limit={}".format(url, random.randint(9000, 999999)), headers = {'user-agent': 'Mozilla/5.0'})
    
    # List to store urls and the following one to validate file format
    content_list = []
    formats = ["jpeg", "jpg", "png"]
    
    # Loop through all url and validate against permitted formats
    for post in r.json()['data']['children']:
        
        try:
            if ([ele for ele in formats if(ele in post['data']['url'])]):
                content_list.append(post['data']['url'])
            else:
                content_list.append(post['data']['selftext'])
        except Excetions as e:
            return e
    
    # Return the list of image urls
    return (content_list)
