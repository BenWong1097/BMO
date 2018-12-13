'''main.py - BMO (Braille More)
    - Takes a picture with an attached rpi camera
    - Processes the text from the image and puts it in a textfile
    - Moves motors to represent braille characters
    - Hooks up two buttons to control which characters are shown, and when to take a new image
'''

from servo import *
from time import sleep
from subprocess import call
from datetime import datetime

import pigpio
from picamera import PiCamera
import camera

import os
os.chdir('/home/pi/Desktop')

BUTTON1 = 12
BUTTON2 = 6
DELAY = 0.2
DELAY_CHAR = 0.5
OUTER_TIME_OUT = 3
INNER_TIME_OUT = 100
NUM_CHAR = 1
#Braille Character 1
# Motors
s_list = [4, 22, 5, 23, 17, 24]
# Motor tuning constants
s_tuning_list = [1, 0.5, .65, .8, 1.5, 1.85]
s_tuning_off_list = [0.33, 1.65, 1, .3, 2, .76]

#Braille Character 2
s2_list = []
# Motors
s2_tuning_list = []
#Motor tuning constants
s2_tuning_off_list = [0.33, 1.65, 1, .3, 2, .76]
char_i = 0
session = 0

def next_char(gpio, level, tick):
    '''next_char switches to the next set of characters'''
    global char_i
    print('Button1 press')
    if level == 0:
        print(char_i)
        char_i = char_i + NUM_CHAR

def next_session(gpio, level, tick):
    '''next_session switches to the next session (camera snap -> new braille set)'''
    global session
    print('Button2 press')
    session = session + 1


def log_output(file_name, data):
    '''log_output logs to a file'''
    f = open(file_name,'a')
    f.write(data)
    print('[%s]: %s' % (str(datetime.now()), data))
    f.write(str(datetime.now()))
    f.write('\n')
    f.close()

log_output('OUTPUT.txt', '-----------------\nStarted main.py... ')
print(os.getcwd())

try:
    #Wait to make sure everything is stable after reboot?
    sleep(5)

    log_output('OUTPUT.txt', 'Commencing main.py... ')

    #Initialize pi gpio
    pi = pigpio.pi()
    pi.set_mode(BUTTON1, pigpio.INPUT)
    pi.set_mode(BUTTON2, pigpio.INPUT)
    pi.set_pull_up_down(BUTTON1, pigpio.PUD_UP)
    pi.set_pull_up_down(BUTTON2, pigpio.PUD_UP)
    pi.callback(BUTTON1, pigpio.EITHER_EDGE, next_char)
    pi.callback(BUTTON2, pigpio.EITHER_EDGE, next_session)

    local_session = -1
    iter_outer_total = 0
    s_on_list = [0] * len(s_list)
    s2_on_list = [0] * len(s2_list)
    #Dead loop
    while iter_outer_total < OUTER_TIME_OUT:
        iter_outer_total = iter_outer_total + 1
        if local_session != session:
            for s in s_on_list:
                if s == 1:
                    if s_list[i] == 24:
                        servo_on(pi, s_list[i], s_tuning_list[i])
                    else:
                        servo_off(pi, s_list[i], s_tuning_off_list[i])
            s_on_list = [0] * len(s_list)
            braille = camera.get_text()
            local_session = session

            char_i = 0
            temp_char_i = char_i
            iter_total = 0
            #Loop: braille characters
            while ((char_i < len(braille)) and (session == local_session) and iter_total < INNER_TIME_OUT):
                iter_total = iter_total + 1
                if char_i != temp_char_i:
                    iter_total = 0
                    temp_char_i = char_i
                char_grid = braille[char_i]
                
                print(char_grid)
                #Loop character 1
                for i in range(0, len(s_list)):
                    if char_grid[i] == 1:
                        if s_on_list[i] == 0:
                            s_on_list[i] = 1
                            if (s_list[i] == 24):
                                print('24')
                                servo_off(pi, s_list[i], s_tuning_off_list[i])
                            else:
                                servo_on(pi, s_list[i], s_tuning_list[i])
                    elif char_grid[i] == 0:
                        if s_on_list[i] == 1:
                            s_on_list[i] = 0
                            if (s_list[i] == 24):
                                servo_on(pi, s_list[i], s_tuning_list[i])
                            else:
                                servo_off(pi, s_list[i], s_tuning_off_list[i])
                    sleep(DELAY_CHAR)
                
                char2_grid = braille[char_i + 1]
                #Loop character 2
                for i in range(0, len(s2_list)):
                    if char2_grid[i] == 1:
                        if s2_on_list[i] == 0:
                            s2_on_list[i] = 1
                            servo_on(pi, s2_list[i], s2_tuning_list[i])
                    elif char2_grid[i] == 0:
                        if s2_on_list[i] == 1:
                            s2_on_list[i] = 0
                            servo_off(pi, s2_list[i], s2_tuning_off_list[i])
                print('')
                sleep(DELAY)
            else:
                sleep(DELAY)

except Exception as e:
    log_output('OUTPUT.txt', ('Error:\n%s' % str(e)))

finally:
    log_output('OUTPUT.txt', 'Exited main.py...')


def render_braille(gpio, level, tick):
    global session
    global char_i
    #Initialize variables
    s_on_list = [0] * len(s_list)
    s2_on_list = [0] * len(s2_list)
    session = session + 1
    local_session = session
    char_i = 0

    #Get braille
    braille = camera.get_text()

    #Loop: braille characters
    while ((char_i < len(braille)) and session == local_session):
        char_grid = braille[char_i]
        print(char_grid[0])
        #Loop character 1
        for i in range(0, len(s_list)):
            if char_grid[i] == 1:
                if s_on_list[i] == 0:
                    s_on_list[i] = 1
                    servo_on(pi, s_list[i], s_tuning_list[i])
            elif char_grid[i] == 0:
                if s_on_list[i] == 1:
                    s_on_list[i] = 0
                    servo_off(pi, s_list[i], s_tuning_list[i])
        char2_grid = braille[char_i + 1]
        #Loop character 2
        for i in range(0, len(s2_list)):
            if char2_grid[i] == 1:
                if s2_on_list[i] == 0:
                    s2_on_list[i] = 1
                    servo_on(pi, s2_list[i], s2_tuning_list[i])
            elif char2_grid[i] == 0:
                if s2_on_list[i] == 1:
                    s2_on_list[i] = 0
                    servo_off(pi, s2_list[i], s2_tuning_list[i])
        sleep(DELAY)