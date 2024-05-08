#!/usr/bin/env pybricks-micropython
from robot import Bot
from zone import Zone
from gui_manager import MainMenu
from color_data import COLORS, ClassifyColor

import threading

COLOR = COLORS.AIR
bot = Bot()

zones = [
    Zone(0, COLORS.GREEN, False), Zone(45, COLORS.BLUE, False),
    Zone(110, COLORS.AIR, True), Zone(135, COLORS.RED, False),
    Zone(210, COLORS.YELLOW, False)
]

# A basic operation for sorting
input_zone = 2
def sort_process(_bot:Bot):
    _bot.get_block(zones[input_zone])

    color = ClassifyColor(_bot.getColorRGB())
    target_zone = None
    for i in zones:
        if(i.color == color):
            target_zone = i
            break
    _bot.placeBlockAtZone(target_zone)

# Initialization of the mechanical features.
def logical_unit(_bot:Bot):
    _bot.calibrateYawMotor()
    _bot.calibratePitchMotor()
    _bot.calibrateClawMotor()

    for i in range(3):
        sort_process(_bot)
    #_bot.moveBlockToZone(zones[2], zones[4]) //This is to showcase the use of moveBlockToZone. <- An example case.

logic_thread = threading.Thread(target=logical_unit, args=(bot,))

logic_thread.start()

main_menu = MainMenu(bot)
main_menu.render()

# I run the mechanical functions on a seperate thread, since the GUI thread is typically the main process thread in a computer.
# Meaning if I want to render anything onto the screen, only the main process has access to that in my program.
# Therefor requiring logical units to run on a seperate thread for parallel execution.