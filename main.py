
# This is a simple bot to open and close tabs in Brave

import pyautogui as pyautogui
import random
import time


def make_money():
    print("Waiting 5 seconds before the proces")
    # Infinite execution
    while True:
        # Open 10 tabs
        for i in range(10):
            # Wait between 3 and 6 seconds for each tab to open
            time_delay = random.randrange(3, 6)
            time.sleep(time_delay)
            with pyautogui.hold('ctrl'):
                pyautogui.press(['t'])
        # Close 10 tabs
        for i in range(10):
            # Wait between 3 and 6 seconds for each tab to close
            time_delay = random.randrange(3, 6)
            time.sleep(time_delay)
            with pyautogui.hold('ctrl'):
                pyautogui.press(['w'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    make_money()
