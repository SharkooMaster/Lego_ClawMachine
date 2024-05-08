import math
from robot import Bot
from pybricks.parameters import Button
from pybricks.media.ev3dev import Font
import time

# A GUI declaration and manager for rendering applications onto the LegoBots screen.

class MainMenu:
    def __init__(self, _bot:Bot):
        self.bot = _bot
        self.ev3 = _bot.ev3
        self.screen_height  =_bot.ev3.screen.height
        self.screen_width   =_bot.ev3.screen.width
    
    def getButtonDown(self):
        target_button = self.ev3.buttons.pressed()
        if(len(target_button) > 0): return target_button[0]
        return None
    
    def draw_main(self, _choice = 0, _frame = 0):
        char_size = 10
        
        alternatives = ["Start", "Settings", "Quit"]
        alternatives_desc = ["Start sorting Legos", "Configure the robots parameters", "Quit the program"]
        char_size = char_size * (len(max(alternatives, key=len)) + 1)

        if(_frame % 3 == 0): alternatives[_choice] = " " * len(alternatives[_choice])
        alternatives[_choice] = ">" + alternatives[_choice]

        self.ev3.screen.draw_box(1, 1, char_size + 1, self.screen_height - 1)
        self.ev3.screen.draw_box(char_size + 3, 1, self.screen_width - 3, self.screen_height - 1)

        for i in range(len(alternatives)):
            self.ev3.screen.draw_text(2, 2 + (i * 16), alternatives[i])
        
        center_box_2 = (self.screen_width - 3) - ((char_size + 3) / 2)
        for i in range(self.screen_height):
            sin_d = math.sin(2*math.pi*0.2 * (_frame + (i/10))) * 5
            self.ev3.screen.draw_text(center_box_2 + (sin_d * 4), i + 1, "*")
    
    def render(self):
        button_choice = 0
        frame = 0
        max_choice = 3

        self.ev3.screen.set_font(Font("Lucida", 16))

        while(True):
            button_down = self.getButtonDown()

            if(button_down == Button.DOWN): button_choice += 1
            elif(button_down == Button.UP):   button_choice -= 1

            if(button_choice < 0): button_choice = max_choice - 1
            elif(button_choice >= max_choice): button_choice = 0

            self.draw_main(button_choice, frame)
            time.sleep(0.4)
            frame += 1
            self.ev3.screen.clear()
