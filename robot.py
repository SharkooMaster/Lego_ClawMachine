from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait

from zone import Zone

class Bot:
    def __init__(self):
        self.YAW_CALIBRATION_OFFSET     = 0
        self.PITCH_CALIBRATION_OFFSET   = 0
        self.CLAW_CALIBRATION_OFFSET    = 0

        self.YAW_SPEED  = 100
        self.PITCH_SPEED= 100
        self.CLAW_SPEED = 100
        self.ev3 = EV3Brick()

        self.claw_motor  = Motor(Port.A)
        self.pitch_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [ 8, 40])
        self.yaw_motor   = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])

        self.color_sensor  = ColorSensor(Port.S2)
        self.touch_sensor  = TouchSensor(Port.S1)

        self.block_held = False
    
    def getColorRGB(self):
        return self.color_sensor.rgb()
    
    def getColorBW(self):
        return self.color_sensor.ambient()
    
    def calibrateYawMotor(self):
        self.yaw_motor.run(-60)
        while not self.touch_sensor.pressed():
            wait(10)
        self.yaw_motor.reset_angle(0)
        self.yaw_motor.hold()
        self.YAW_CALIBRATION_OFFSET = self.yaw_motor.angle()
    
    def calibratePitchMotor(self):
        print("pitch")
        self.pitch_motor.run_until_stalled(-30, duty_limit=30)
        self.pitch_motor.stop()
        self.pitch_motor.reset_angle(0)
        self.PITCH_CALIBRATION_OFFSET = 0
        print("pitch done")

    def calibrateClawMotor(self):
        print("Claw")
        self.claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
        self.claw_motor.reset_angle(0)
        self.claw_motor.run_target(200, -90)
        self.CLAW_CALIBRATION_OFFSET = self.claw_motor.angle()
        print("pitch done")
    
    def rotateToZone(self, _zone:Zone):
        self.yaw_motor.run_target(self.YAW_SPEED, _zone.pos_angle)
    
    def get_block(self, _zone:Zone):
        self.ev3.speaker.beep()
        self.pitch_motor.run_target(20, 90)
        self.rotateToZone(_zone)
        self.pitch_motor.run_target(20, 20 * (1 + _zone.brickCount))
        self.claw_motor.run_until_stalled(200, then=Stop.COAST, duty_limit=50)
        if(self.claw_motor.angle() < -4):
            self.block_held = True
            self.claw_motor.hold()
            print("HOLDING BLOCK")
        else: self.block_held = False
        self.pitch_motor.run_target(20, 70)
        print(self.claw_motor.angle())
    
    def moveBlockToZone(self, _from_zone, _to_zone):
        self.get_block(_from_zone)
        if(self.block_held):
            self.pitch_motor.run_target(20, 90)
            self.rotateToZone(_to_zone)
            self.pitch_motor.run_target(20, 4 + (20 * _to_zone.brickCount))
            self.claw_motor.run_angle(40, -30)
    
    def placeBlockAtZone(self, _to_zone):
        if(self.block_held):
            self.pitch_motor.run_target(20, 90)
            self.rotateToZone(_to_zone)
            self.pitch_motor.run_target(20, 4 + (20 * _to_zone.brickCount))
            self.claw_motor.run_angle(40, -30)
            self.pitch_motor.run_target(20, 90)
