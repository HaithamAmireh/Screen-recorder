import cv2
import numpy as np
import pyautogui
import time
import datetime

SCREENSIZE = (1920,1080)

fourcc = cv2.VideoWriter_fourcc(*"XVID")
time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
file_name = f'{time_stamp}.avi'

FPS = 60
out = cv2.VideoWriter(file_name, fourcc, 20.0 , (SCREENSIZE))

prev = 0

while True:
    time_elapsed = time.time() - prev

    img = pyautogui.screenshot()

    if time_elapsed > 1.0/FPS:
        prev= time.time()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
    time.sleep(1/FPS)
cv2.destroyAllWindows()
out.release()