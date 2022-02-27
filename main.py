
# This is a simple bot to open and close tabs in Brave

import pyautogui as pyautogui
import random
import time
from constants import *

def random_mouse_movements():
    number_of_moves = random.randrange(MIN_MOVEMENTS, MAX_MOVEMENTS)
    for i in range(number_of_moves):
        # Moves mouse to coordinates X and Y , with time_delay
        x = random.randrange(MIN_X_PIXELS, MAX_X_PIXELS)
        y = random.randrange(MIN_Y_PIXELS, MAX_Y_PIXELS)
        pyautogui.moveTo(x, y, 2)

def random_wait():
    time_delay = random.randrange(MIN_WAIT, MAX_WAIT)
    time.sleep(time_delay)


def make_money():
    print("Waiting 8 seconds before the process")
    time.sleep(8)
    # Infinite execution
    while True:
        number_of_tabs = random.randrange(MIN_NUMBER_TABS, MAX_NUMBER_TABS)
        # Open 10 tabs
        for i in range(number_of_tabs):
            random_wait()
            with pyautogui.hold('ctrl'):
                pyautogui.press(['t'])
            random_mouse_movements()
        # Close 10 tabs
        for i in range(number_of_tabs):
            random_wait()
            with pyautogui.hold('ctrl'):
                pyautogui.press(['w'])
                random_mouse_movements()
        time_delay = random.randrange(MIN_SLEEP_TIME, MAX_SLEEP_TIME)
        time.sleep(time_delay)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_money()
