import time
import pigpio

SERVO_ON_STRENGTH = 1550
SERVO_OFF_STRENGTH = 1450

def servo_on(pi, pin, tune=1):
    '''servo_on(pi: PigpioPi, pin: Integer, tune: Float'''
    pi.set_servo_pulsewidth(pin, SERVO_ON_STRENGTH)
    time.sleep(.3*tune)
    pi.set_servo_pulsewidth(pin, 0)
    
def servo_off(pi, pin, tune=1):
    '''servo_off(pi: PigpioPi, pin: Integer, tune: Float'''
    pi.set_servo_pulsewidth(pin, SERVO_OFF_STRENGTH)
    time.sleep(.3*tune)
    pi.set_servo_pulsewidth(pin, 0)
