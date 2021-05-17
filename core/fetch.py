# Imports
import json
import requests

# Set colors
red = "\033[91m"
reset = "\033[0m"

# Get a list of image url from a supplied subreddit and category 
def get_img(sub, cat):
    """ Fetch image url links of a subreddit via .json method.

    Args:
        sub([string]): Subreddit name.
        cat([string]): Catagory type (top, rising, etc).

    Returns:
        image_lsit([list]): Returns a list of urls of scraped images.
    """

    number = 99999
    url = "https://www.reddit.com/r/{}/{}/".format(sub,cat)
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
        
