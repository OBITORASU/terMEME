import subprocess
import sys
import time

from core.banner import banner
from core.scrape import *

# Define colors 
red = "\033[91m"
green = "\033[92m"    
reset = "\033[0m"

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

    # Fetch the image url based on the user set parameters and display them        
    if ch==1:
        print("%s[+] Fetching the top images from r/{}....".format(sub)%(green))
        print()  
        time.sleep(1)
        result = get_img(sub, "top")
        # Used an if else in all cases to check whether result is false or has the list
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==2:
        print("%s[+] Fetching the new images from r/{}....".format(sub)%(green))
        print()
        time.sleep(1)
        result = get_img(sub, "new")
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==3:
        print("%s[+] Fetching the hot images from r/{}....".format(sub)%(green))
        print()
        time.sleep(1)
        result = get_img(sub, "hot")
        if not result:
            sys.exit(1)
        else: 
            display(result)

    elif ch==4:
        print("%s[+] Fetching the rising images from r/{}....".format(sub)%(green))
        print()
        time.sleep(1)
        result = get_img(sub, "rising")
        if not result:
            sys.exit(1)
        else: 
            display(result)
    

if __name__=="__main__": 
    try:
        main()
    except KeyboardInterrupt:
        print("\n%s[-] SIGTERM recievied terminating...%s"%(red,reset))
        sys.exit(1)
