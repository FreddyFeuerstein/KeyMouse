import keyboard  # using module keyboard
import mouse # using module mouse
import time # using module time
import os # using module os
import sys # using module sys

speed=0.05 # lower = faster
print(' Aa -> [|] KeyMouse (c)2020 Freddy F.')

if os.geteuid() != 0:
    print("You can only use this program as root. Try running it with sudo next time.")
    exit()

while 1 <= 10:
    if keyboard.is_pressed('i'):  #up
        mouse.move(0, -20, absolute=False, duration=speed)
    if keyboard.is_pressed('k'):  #down
        mouse.move(0, 20, absolute=False, duration=speed)
    if keyboard.is_pressed('j'):  #left
        mouse.move(-20, 0, absolute=False, duration=speed)
    if keyboard.is_pressed('l'):  # Right
        mouse.move(20, 0, absolute=False, duration=speed)
    if keyboard.is_pressed('u'):  # Left Click
        mouse.click('left')
        time.sleep(speed * 100)
    if keyboard.is_pressed('p'):  # Middle Click
        mouse.click('middle')
        time.sleep(speed * 100)
    if keyboard.is_pressed('o'):  # Right Click
        mouse.click('right')
        time.sleep(speed * 100)
