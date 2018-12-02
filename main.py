#import RPi.GPIO as GPIO
from picamera import PiCamera

import camera
import pigpio
from servo import *
from time import sleep
from subprocess import call

BUTTON1 = 12
BUTTON2 = 13
DELAY = 0.1
s_list = [23]
s2_list = []
char_i = 0
session = 0
def next_char(gpio, level, tick):
    global char_i
    print('Button1 press')
    if level == 0:
        print(char_i)
        char_i = char_i + 1

def next_session(gpio, level, tick):
    global session
    print('Button2 press')
    session = session + 1

def render_braille(gpio, level, tick):
    global session
    global char_i
    s_on_list = [0] * len(s_list)
    s2_on_list = [0] * len(s2_list)
    braille = camera.get_text()
    session = session + 1
    local_session = session
    #GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback=next_char, bouncetime = 300)
    char_i = 0
    while ((char_i < len(braille)) and session == local_session):
    #for char_grid in braille:
        char_grid = braille[char_i]
        print(char_grid[0])
        for i in range(0, len(s_list)):
            if char_grid[i] == 1:
                if s_on_list[i] == 0:
                    s_on_list[i] = 1
                    servo_on(pi, s_list[i])
            elif char_grid[i] == 0:
                if s_on_list[i] == 1:
                    s_on_list[i] = 0
                    servo_off(pi, s_list[i])
        char2_grid = braille[char_i + 1]
        for i in range(0, len(s2_list)):
            if char2_grid[i] == 1:
                if s2_on_list[i] == 0:
                    s2_on_list[i] = 1
                    servo_on(pi, s2_list[i])
            elif char2_grid[i] == 0:
                if s2_on_list[i] == 1:
                    s2_on_list[i] = 0
                    servo_off(pi, s2_list[i])
        sleep(DELAY)
        
try:
    # call(["sudo", "pigpiod"])
    sleep(5)
    pi = pigpio.pi()
    pi.set_mode(BUTTON1, pigpio.INPUT)
    pi.set_mode(BUTTON2, pigpio.INPUT)
    pi.set_pull_up_down(BUTTON1, pigpio.PUD_UP)
    pi.set_pull_up_down(BUTTON2, pigpio.PUD_UP)
    pi.callback(BUTTON1, pigpio.EITHER_EDGE, next_char)
    pi.callback(BUTTON2, pigpio.EITHER_EDGE, next_session)

    local_session = 0
    while True:
        if local_session != session:
            s_on_list = [0] * len(s_list)
            s2_on_list = [0] * len(s2_list)
            braille = camera.get_text()
            local_session = session
            #GPIO.add_event_detect(BUTTON1, GPIO.RISING, callback=next_char, bouncetime = 300)
            char_i = 0
            while ((char_i < len(braille)) and session == local_session):
            #for char_grid in braille:
                char_grid = braille[char_i]
                print(char_grid[0])
                for i in range(0, len(s_list)):
                    if char_grid[i] == 1:
                        if s_on_list[i] == 0:
                            s_on_list[i] = 1
                            servo_on(pi, s_list[i])
                    elif char_grid[i] == 0:
                        if s_on_list[i] == 1:
                            s_on_list[i] = 0
                            servo_off(pi, s_list[i])
                char2_grid = braille[char_i + 1]
                for i in range(0, len(s2_list)):
                    if char2_grid[i] == 1:
                        if s2_on_list[i] == 0:
                            s2_on_list[i] = 1
                            servo_on(pi, s2_list[i])
                    elif char2_grid[i] == 0:
                        if s2_on_list[i] == 1:
                            s2_on_list[i] = 0
                            servo_off(pi, s2_list[i])
                sleep(DELAY)
            else:
                sleep(DELAY)
        # sleep(5)
    #    print(char_i)
    #    print( pi.read(BUTTON1))
except:
    # call(["sudo", "killall", "pigpiod"])
    print('oops')