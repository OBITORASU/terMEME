# Imports
import subprocess
import sys
import time

from core.banner import banner
from core.fetch import get_img
from core.display import display_img
from core.validate import check_validity

# Define colors 
red = "\033[91m"
green = "\033[92m"    
reset = "\033[0m"

 # Make dictionary for choices
choices = {1:"top", 2: "new", 3: "hot",4: "rising"}

# Function to fetch images and display them
def get_memes(choice, sub):
    """ Fetch the result list containing image urls for given subreddit and display them 
    using w3m-img inside the terminal.

    Args:
        choice ([int]): An integer corresponding to a category like top, new and so on.
        sub ([str]): Subreddit of the user's choice.
    """

    category = choices[choice]
    print("%s[+] Fetching the {} images from r/{}....".format(category,sub)%(green))
    print()
    time.sleep(1)
    result = get_img(sub, category)
    if not result:
        sys.exit(1)
    else: 
        display_img(result)

# Main function
def main():
    # Clear up the terminal screen
    subprocess.call("clear", shell=True)
    print(banner())
    print()
    
    # Check the validity of user entered subreddit and assign its value to sub
    sub = check_validity()

    # Category menu
    print ("""%s[+] Wubba Lubba dub-dub!

    Select a Category:
    1) Top
    2) New
    3) Hot
    4) Rising
    5) Exit
    """%(green))

    # Loop until valid category is selected
    while(True):
        
        ch = int(input("%sEnter your choice: %s"%(green, reset)))
        print()
        if ch==1 or ch==2 or ch==3 or ch==4 or ch==5:
            if ch==5:
                sys.exit()
            else:
                break
            
        else:
            print("%s[-] Invalid input detected please enter a valid input!"%(red))
            print()

    # Call function to display image urls fetched for respective sub and category 
    get_memes(ch, sub)
            
# Execute main function and exit upon keyboard interrupt
if __name__=="__main__": 
    try:
        main()
    except KeyboardInterrupt:
        print("\n%s[-] SIGTERM recievied terminating...%s"%(red,reset))
        sys.exit(1)
