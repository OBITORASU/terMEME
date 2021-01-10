import json
import requests
import time

from clint.textui import colored
from urllib.request import urlopen, URLError

# Check subreddit validity if url is invalid return error else return subreddit as sub
def check_validity():
    while True:
        sub = input(colored.green("Enter the name of a valid subreddit: "))
        print()
        print(colored.green("[+] Checking subreddit validity...."))
        print()
        try:
            if sub.isspace():
                print(colored.red("[-] Invalid subreddit"))
                print()
                               
            else:
                urlopen("https://www.reddit.com/r/{}".format(sub))
                print(colored.green("[+] Subreddit found!"))
                print()
                break
                
        except URLError:
            print(colored.red("[-] Invalid subreddit!"))
            print()

    return sub

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
                # Fill the list with image urls
                img_list.append(post['data']['url'])
    
    # If img url list is empty return false
    if not img_list:
        print(colored.red("[-] Back luck partner! No images found in subreddit :("))
        print()
        return False
    # Return the list of image urls
    else:
        return (img_list)





