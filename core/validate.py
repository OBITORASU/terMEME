# Imports
from urllib.request import urlopen, URLError

# Set colors
red = "\033[91m"
green = "\033[92m"    

# Check subreddit validity if url is invalid return error else return subreddit as sub
def check_validity():
    """ Check validity of a subreddit.

    Returns:
        sub([string]): Returns the name of the subreddit if it is valid.
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

            # Trying opening the url to validate                 
            else:
                urlopen("https://www.reddit.com/r/{}".format(sub))
                print("%s[+] Subreddit found!"%(green))
                print()
                break
        # URL is invalid for URLError exception 
        except URLError:
            print("%s[-] Invalid subreddit!"%(red))
            print()

    return sub
