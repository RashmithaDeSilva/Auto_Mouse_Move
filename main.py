import pyautogui
import time

def touch_mouse_every_30_seconds():
    while True:
        # Move the mouse slightly to the right and then back to the original position
        current_position = pyautogui.position()
        pyautogui.move(50, 0)  # Move the mouse 10 pixels to the right
        time.sleep(30) # Wait for 30 seconds
        pyautogui.move(-50, 0)  # Move the mouse back to the original position
        time.sleep(30) # Wait for 30 seconds

if __name__ == "__main__":
    touch_mouse_every_30_seconds()
