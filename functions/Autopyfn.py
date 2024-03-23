import time
import pyautogui
import webbrowser
import os
import requests
import bs4 as Bs
from selenium import webdriver

pyautogui.useImageNotFoundException()

def clickButtonInWeb(image_path,url):
    # current_directory = os.path.dirname(__file__)
    # image_path = os.path.join(current_directory, fileName, imgName)
    # image_path = os.path.join(current_directory, 'images', 'spotifyPlayButton.png')
    webbrowser.open(url, new=2) 
    #load till the image is found
    response= requests.get(url)
    if response.status_code == 200:
        while True:
            try:
                print("FOUND!")
   
                buttonx, buttony = pyautogui.locateCenterOnScreen(image_path,confidence=0.9)
                print("button_corrd:",buttonx,buttony)
                pyautogui.click(buttonx, buttony)
                break
            except pyautogui.ImageNotFoundException:
                    print('NO FOUND!')
    else:
        print("ERROR WHILE OPENING PAGE")
def clickSpotifyPlayButton(url,conf):
    spotify_play_button='c:/Users/radin/Documents/Adi light/Code/AIVA beta/images/spotifyPlayButton.png'

    response= requests.get(url)
    if response.status_code == 200:
        while True:
            try:
                print("FOUND!")
                buttonx, buttony = pyautogui.locateCenterOnScreen(spotify_play_button,confidence=conf,grayscale=False)
                print("button_corrd:",buttonx,buttony)
                pyautogui.click(buttonx, buttony)
                break
            except pyautogui.ImageNotFoundException:
                    print('NO FOUND!')
    else:
        print("ERROR WHILE OPENING PAGE")
