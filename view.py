import subprocess
import sys
import random

subprocess.call("clear", shell=True)

from urllib.request import urlopen, URLError
from getch import getch
from clint.textui import colored
from banner import banner
from meme import get_meme



def display(result):
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

while(True):
    sub = input(colored.green("Enter the name of a valid subreddit: "))
    print()
    print(colored.green("[+] Checking subreddit validity...."))
    print()
    try:
        urlopen("https://www.reddit.com/r/{}".format(sub))
        print(colored.green("[+] Subreddit found!"))
        print()
        break
    except URLError:
        print(colored.green("[-] Invalid subreddit!"))
        print()



print (colored.green("""Wubba Lubba dub-dub
Select a Category:
1) Top
2) New
3) Hot
4) Rising
5) Exit
"""))

while(True):
    
    ch = int(input(colored.green("Enter your choice: ")))
    if ch==1 or ch==2 or ch==3 or ch==4 or ch==5:
        if ch==5:
            sys.exit()
        else:
            break
        
    else:
        print(colored.red("[-] Invalid input detected please enter a valid input!"))
        print()

if ch==1:
    print(colored.green("[+] Fetching the top memes from {}....".format(sub)))  
    result = get_meme(sub, "top")  
    display(result)

elif ch==2:
    print(colored.green("[+] Fetching the new memes from {}....".format(sub)))
    result = get_meme(sub, "new")
    display(result)

elif ch==3:
    print(colored.green("[+] Fetching the hot memes from {}....".format(sub)))
    result = get_meme(sub, "hot")
    display(result)

elif ch==4:
    print(colored.green("[+] Fetching the rising memes from {}....".format(sub)))
    result = get_meme(sub, "rising")
    display(result)


