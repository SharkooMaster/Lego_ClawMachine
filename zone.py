
from color_data import COLORS

# Zone stands for the position (container) that you want to declare and define for the purpose of sorting.

class Zone:
    def __init__(self, _angle, _color, _isInput):
        self.pos_angle = _angle
        self.color = _color
        self.isInput = _isInput
        self.brickCount = 0