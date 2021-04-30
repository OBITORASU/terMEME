# terMEME
## A scrapper which displays random images from a subreddit of your choice inside your linux terminal.

terMEME is a terminal based web scraper written in Python 3 which allows Linux users to view random images from subreddits inside the comfort of their terminals.

**NOTE:**  Best use suggestion is to browse memes (hence the name) but it works for any/all images. Also keep in mind not all terminals are support w3m-img (it is a hack) and might resort to displaying the image externally using imagemagick, some of the supported terminals are ```konsole, xterm, Gnome-terminal```.

## Dependencies 

- `w3m-img or imlib2`
    - For image rendering inside the terminal.
- `imagemagick`
    - If your terminal has trouble rendering the images, it will have the option to display the image externally.

## Python Dependencies 

All the python dependencies for this project are listed in the ```requirements.txt```.

## Installation 
```
git clone https://github.com/OBITORASU/terMEME.git
cd terMEME
pip3 install -r requirements.txt

(Debian)
sudo apt-get install w3m-img
sudo apt-get install imagemagick

(Arch)
sudo pacman -S w3m imlib2 imagemagick
```
With the above done, you are ready to go. Fire up the script by running:
```
python3 view.py
```
## Navigation
Use your q key to quit the w3m preview inside your terminal. On the prompt pressing e will terminate the program and any other key will bombard you with more random images. If your terminal is incapable of displaying the images in it, it will switch you to an external view on imagemagick. In the second case pressing q twice will get you back to the prompt by quitting the preview for both imagemagick and w3m.

---
**NOTE:**

**Sometimes validating the subreddit might result in false positives, if you are certain the entered subreddit exists just try again and it should work.**

---
