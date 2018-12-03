from subprocess import call
from picamera import PiCamera
from time import sleep
import braille_characters as bc

def get_text():
    #camera = PiCamera()

    #camera.start_preview()
    #sleep(5)
    #camera.capture('/home/pi/Desktop/imageTest.jpg')
    #camera.stop_preview()
    
    call(["raspistill", "-o", "imageTest.jpg"])
    call(["tesseract", "imageTest.jpg", "testfile"])
    
    data = open("testfile.txt", "r")
    words = data.read()
    output = ""
    output = output.join([ char if (char.isalnum() or char == ' ') else '' for char in words])
    output = output.strip()
    print(output)
    output_braille = list(map(bc.toBraille, output))
    
    #output_braille = [[0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0]] * 2
    print(output_braille)
    return output_braille