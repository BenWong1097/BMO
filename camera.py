from subprocess import call
from picamera import PiCamera
from time import sleep
import braille_characters as bc

OUTPUT_IMAGE = 'imageTest.jpg'
OUTPUT_FILE = 'testfile.txt'

def get_text():
    '''get_text(): Integer[6][]
        Takes an image from a connected RaspberryPi Camera and processes it
        into an array representation of braille characters.
        Writes it out in a textfile.
    '''
    call(["raspistill", "-o", OUTPUT_IMAGE])
    call(["tesseract", OUTPUT_IMAGE, "testfile"])
    
    data = open(OUTPUT_FILE, "r")
    words = data.read()
    output = ""
    output = output.join([ char if (char.isalnum() or char == ' ') else '' for char in words])
    output = output.strip()
    print(output)
    output_braille = list(map(bc.toBraille, output))
    
    #For testing motor functionality
    #output_braille = [[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0]] * 2
    print(output_braille)
    return output_braille