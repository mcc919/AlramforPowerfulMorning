import os
import time
import random
import webbrowser

start = time.time()

f = open("C:/Users/kor/Documents/PowerfulMusicList.txt", 'r')
PowerfulMusics = f.read().split("\n")
TodaysMusic = random.choice(PowerfulMusics)
webbrowser.open_new(TodaysMusic)

while True:
    if time.time() - start > 60*20:
        break

os.system("shutdown -s -t 1")