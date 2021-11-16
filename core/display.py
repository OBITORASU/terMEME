# Imports
import random
import sys
import subprocess

from getch import getch

# Set colors
green = "\033[92m"    
reset = "\033[0m"

# Function to display the image urls in results inside the terminal
def display_img(result):
    """ Display images fetched from any subreddit in your terminal.

    Args:
        result([list]): A list of urls which you want to display.
    """

    lst = []
    while True:
        url = random.choice(result)
        if url not in lst:
            subprocess.call(["w3m", "-o", "ext_image_viewer=false", "-o", "confirm_qq=false", url])
            subprocess.call(["clear"])
            lst.append(url)
            print("%sPress 'e' to exit or any other key to continue....%s"%(green, reset))
            key = getch()
            if key=="e":
                subprocess.call(["clear"])
                sys.exit()
