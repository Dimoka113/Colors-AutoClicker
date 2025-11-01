from pynput.mouse import Button, Controller
import pyautogui as pgui
import json, keyboard, sys, time
from clicker import Clicker


clicks = Clicker(path_cfg="config.json")
data = clicks.get_data()

def run():
    for trigger in data[0]:
        if (clicks.check(trigger[0], trigger[1])):
            clicks.press(data[1][trigger[2]])



def main(key_exit: str):
    print("Программа запущена. Нажми {key}, чтобы остановить.".format(key=key_exit))
    while True:
        run()
        if keyboard.is_pressed('{key}'.format(key=key_exit)):
            print("{key} нажата. Остановка кликов...".format(key=key_exit))
            sys.exit(0)

        time.sleep(0.01)

if __name__ == "__main__":
    main(clicks.get_exit_key())