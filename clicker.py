from defs import Defs
from pynput.mouse import Button, Controller
import pyautogui as pgui


class Clicker(Defs):
    config = None; allScreens = None; triggers = None; where = None; stop = False; 


    def __init__(self, path_cfg: str):
        self.config = self.get_json(path_cfg)
        self.allScreens = self.config["allScreens"]
        self.triggers = self.config["triggers"]
        self.where = self.config["where"]

    def get_data(self) -> list:
        return [self.triggers, self.where]
    
    def get_exit_key(self) -> str:
        return self.config["disable_key"]
    
    def check(
            self, 
            region: list[int, int, int, int],
            trigger: list[int,int,int]
            ) -> bool:
        image = pgui.screenshot(region=tuple(region))
        colors = image.getcolors()
        sun_colors = self.sum_pixels(colors)['average']
        
        if list(sun_colors) == trigger:
            return True
        return False

    def press(self, key: list[str, int, int]) -> None:
        buton = getattr(Button, key[0])
        mouse = Controller()
        mouse.position = tuple([key[1], key[2]])
        mouse.click(buton, key[3])
        print("Кликнул")