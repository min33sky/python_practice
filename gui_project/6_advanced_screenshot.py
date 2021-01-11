import time
import keyboard  # pip install keyboard
from PIL import ImageGrab


def screenshot():
    # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)
# keyboard.add_hotkey("ctrl+shift+s", screenshot)

keyboard.wait("esc")
