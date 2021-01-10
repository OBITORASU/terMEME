import subprocess
import sys
import time
import random

# Clear up the terminal screen
subprocess.call("clear", shell=True)

from urllib.request import urlopen, URLError
from getch import getch
from clint.textui import colored
from banner import *
from scrape import *

# Function to display url using w3m-img inside the terminal
def display(result):
    # Appending to a list and checking urls against it to prevent images from reappearing when randomizing 
    lst = []
    while True:
        url = random.choice(result)
        if url not in lst:
            subprocess.call("w3m -o ext_image_viewer=false -o confirm_qq=false {}".format(url), shell=True)
            subprocess.call("clear", shell=True)
            lst.append(url)
            print(colored.green("Press e to exit or any other key to continue...."))
            key = getch()
            if key=="e":
                subprocess.call("clear", shell=True)
                sys.exit()

print(banner())
print()
sub = check_validity()

# Category menu
print (colored.green("""[+] Wubba Lubba dub-dub!

Select a Category:
1) Top
2) New
3) Hot
4) Rising
5) Exit
"""))

# Loop until valid category is selected
while(True):
    
    ch = int(input(colored.green("Enter your choice: ")))
    print()
    if ch==1 or ch==2 or ch==3 or ch==4 or ch==5:
        if ch==5:
            sys.exit()
        else:
            break
        
    else:
        print(colored.red("[-] Invalid input detected please enter a valid input!"))
        print()

# Fetch the image url based on the user set parameters and display them        
if ch==1:
    print(colored.green("[+] Fetching the top images from r/{}....".format(sub)))
    print()  
    time.sleep(1)
    result = get_img(sub, "top")
    # Used an if else in all cases to check whether result is false or has the list
    if not result:
        sys.exit()
    else: 
        display(result)

elif ch==2:
    print(colored.green("[+] Fetching the new images from r/{}....".format(sub)))
    print()
    time.sleep(1)
    result = get_img(sub, "new")
    if not result:
        sys.exit()
    else: 
        display(result)

elif ch==3:
    print(colored.green("[+] Fetching the hot images from r/{}....".format(sub)))
    print()
    time.sleep(1)
    result = get_img(sub, "hot")
    if not result:
        sys.exit()
    else: 
        display(result)

elif ch==4:
    print(colored.green("[+] Fetching the rising images from r/{}....".format(sub)))
    print()
    time.sleep(1)
    result = get_img(sub, "rising")
    if not result:
        sys.exit()
    else: 
        display(result)
    



