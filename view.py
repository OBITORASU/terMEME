import subprocess
import sys
import time
import random
from getch import getch


from banner import *
from scrape import *

# Clear up the terminal screen
subprocess.call("clear", shell=True)

# Function to display url using w3m-content inside the terminal
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

def paste(result):

    lst = []
    while True:
        text = random.choice(result)
        if text not in lst:
            subprocess.call("clear", shell=True)
            lst.append(text)
            print(colored.green("Press e to exit or any other key to continue...."))
            print(text)
            key = getch()
            if key=="e":
                subprocess.call("clear", shell=True)
                sys.exit()

def menu():
    menu = {"1":"top","2":"new","3":"hot","4":"rising", "0":"exit"}
    print(colored.green(f"""Wubba Lubba dub-dub!\nSelect a Category:\n"""))
    for i in menu.values():
        print(i,"\n")
    choice=input("Enter your choice: ")
    return menu.get(choice, "Invalid Choice")


def get_categories(sub, choice):
    print(colored.green("[+] Fetching the {} memes from r/{}....".format(choice, sub)))  
    time.sleep(1)
    result = get_content(sub, choice) 
    for reddits in result:
        print(reddits)
        if reddits.endswith('jpg') or reddits.endswith("jpg") or reddits.endswith("png"):
            display(result)
        else:
            paste(result)


if __name__ == "__main__":

    print(banner())

    sub = check_validity()

    while True:
        get_categories(sub, menu())

