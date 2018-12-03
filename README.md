# BMO
CSCE 462 Project: Braille More

## Team Members
* Benjamin Wong
* Omer Fiazuddin

## Concept

We are creating a braille machine that will convert text into physical braille. Most people don’t know how braille is designed and read. Our prototype will serve as a learning machine for people to become familiar with braille writing system as well as serve visually impaired people to read any written text in English.

Our device will include a platform on which the text document will be placed. The device will also have a frame to overlay the platform with the purpose of isolating the content of the document. A raspberry pi will be utilized as the processor, with a camera and button acting as input and braille display acting as an output.

In order to detect the text, a camera will be equipped and positioned so that it is able to have a full view of the document. This camera will be interfaced to a raspberry pi, which will act as the processor. To activate the camera, a button, attached to the platform will need to be pressed.

The raspberry pi will be in charge of performing the conversion of text to braille. In order to convert text into Braille, the image input will go through and recognize each braille character and convert each to their corresponding text. Of course, the program will have a mapping of which pattern corresponds to which braille character. Once all of the text has been converted into braille, the data will be fed to an output device connected to the raspberry pi in the form of a braille display device which will be attached to the side of the platform. The braille display will be able to display 2 braille characters.

## Main Demo

https://youtu.be/oRpzyBsLPJg

## Sketch

[BMO Structure Sketch](https://drive.google.com/open?id=1k19HGCnunsLmAbb3jfyHW14Bk5K356jN)

## BMO

[BMO Physical Structure](https://drive.google.com/open?id=1KfdaO0r_1QDDPvPRGU0cTcoC1TXwqPWE)
