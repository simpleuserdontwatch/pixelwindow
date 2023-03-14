import time

import cv2
import numpy as np
import pyautogui

pixrate = int(pyautogui.prompt("resolution"))


def pixelate(img, w, h):
    height, width = img.shape[:2]
    temp = cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)


SCREEN_SIZE = (400, 300)

FRAME_RATE = 150
while True:
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    frame = cv2.resize(frame, SCREEN_SIZE)
    frame = pixelate(frame, pixrate, pixrate)
    cv2.imshow("Pixelated window res: " + str(pixrate), frame)
    cv2.setWindowProperty(
        "Pixelated window res: " + str(pixrate), cv2.WND_PROP_TOPMOST, 1
    )
    if cv2.waitKey(1) == ord("q"):
        break
    time.sleep(1 / FRAME_RATE)

cv2.destroyAllWindows()
