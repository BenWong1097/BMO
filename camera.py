from subprocess import call
from picamera import PiCamera
from time import sleep
import braille_characters as bc

def get_text():
    camera = PiCamera()

    #camera.start_preview()
    #sleep(10)
    #camera.capture('/home/pi/Desktop/imageTest.jpg')
    #camera.stop_preview()
    #img = Image.open('/home/pi/Desktop/raspi_test.png')
    #call(["tesseract", "imageTest.jpg", "testfile"])
    call(["tesseract", "raspi_test.png", "testfile"])
    data = open("testfile.txt", "r")
    words = data.read()
    output = ""
    output = output.join([ char if (char.isalnum() or char == ' ') else '' for char in words])
    
    print(output)
    output_braille = list(map(bc.toBraille, output))
    print(output_braille)
    return output_braille
    #print(bc.toBraille('a'))
