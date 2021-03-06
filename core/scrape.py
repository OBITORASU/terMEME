import json
import requests
import random
import subprocess
import sys

from urllib.request import urlopen, URLError
from getch import getch

red = "\033[91m"
green = "\033[92m"    
reset = "\033[0m"

def display(result):
    """Display images fetched from any subreddit in your terminal.

    Args:
        result (list): A list of urls which you want to display.
    """

    lst = []
    while True:
        url = random.choice(result)
        if url not in lst:
            subprocess.call("w3m -o ext_image_viewer=false -o confirm_qq=false {}".format(url), shell=True)
            subprocess.call("clear", shell=True)
            lst.append(url)
            print("%sPress e to exit or any other key to continue....%s"%(green, reset))
            key = getch()
            if key=="e":
                subprocess.call("clear", shell=True)
                sys.exit()

# Check subreddit validity if url is invalid return error else return subreddit as sub
def check_validity():
    """Check validity of a subreddit.

    Returns:
        sub (string): Returns the name of the subreddit if it is valid.
    """

    while True:
        sub = input("%sEnter the name of a valid subreddit: "%(green))
        print()
        print("%s[+] Checking subreddit validity...."%(green))
        print()
        try:
            if sub.isspace():
                print("%s[-] Invalid subreddit"%(red))
                print()
                               
            else:
                urlopen("https://www.reddit.com/r/{}".format(sub))
                print("%s[+] Subreddit found!"%(green))
                print()
                break
                
        except URLError:
            print("%s[-] Invalid subreddit!"%(red))
            print()

    return sub

# Get a list of image url from a supplied subreddit and category 
def get_img(str1, str2):
    """Fetch image url links of a subreddit via .json method.

    Args:
        str1 (string): Subreddit name.
        str2 (string): Catagory type (top, rising, etc).

    Returns:
        image_lsit (list): Returns a list of urls of scraped images.
    """

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
        print("%s[-] Back luck partner! No images found in subreddit!%s"%(red, reset))
        print()
        return False
    # Return the list of image urls
    else:
        return (img_list)





