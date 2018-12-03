import time
#import wiringpi
import pigpio

#wiringpi.wiringPiSetupGpio()
#wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
#Setup clock
#wiringpi.pwmSetClock(192)
#wiringpi.pwmSetRange(2000)

def servo_setup(pin):
    print("Nothing here to set up")
    #wiringpi.pinMode(pin, wiringpi.GPIO.PWM_OUTPUT)
    #wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
    #wiringpi.pwmSetClock(192)
    #wiringpi.pwmSetRange(2000)
    
def servo_on(pi, pin, tune=1):
    #wiringpi.pwmWrite(pin, 250)
    #pi.set_servo_pulsewidth(pin, 2000)
    pi.set_servo_pulsewidth(pin, 1550)
    time.sleep(.3*tune)
    pi.set_servo_pulsewidth(pin, 0)
    #wiringpi.pwmWrite(pin, 0)
    
def servo_off(pi, pin, tune=1):
    #wiringpi.pwmWrite(pin, 50)
    pi.set_servo_pulsewidth(pin, 1450)
    time.sleep(.3*tune)
    pi.set_servo_pulsewidth(pin, 0)
    #wiringpi.pwmWrite(pin, 0)
