
# This is a simple bot to open and close tabs in Brave

import pyautogui as pyautogui
import random
import time


def make_money():
    print("Waiting 8 seconds before the proces")
    time.sleep(8)
    # Infinite execution
    while True:
        # Open 10 tabs
        for i in range(10):
            # Wait between 8 and 15 seconds for each tab to open
            time_delay = random.randrange(8, 15)
            time.sleep(time_delay)
            with pyautogui.hold('ctrl'):
                pyautogui.press(['t'])
            # Moves mouse to coordinates X and Y , with time_delay
            random_mul = random.randrange(50, 1200)
            pyautogui.moveTo(random_mul, random_mul, 2)
        # Close 10 tabs
        for i in range(10):
            # Wait between 3 and 6 seconds for each tab to close
            time_delay = random.randrange(3, 6)
            time.sleep(time_delay)
            with pyautogui.hold('ctrl'):
                pyautogui.press(['w'])
                # Moves mouse to coordinates X and Y , with time_delay
                random_mul = random.randrange(50, 1200)
                pyautogui.moveTo(random_mul, random_mul, 2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_money()
