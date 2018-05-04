Christopher Meneses
chrismeneses@csu.fullerton.edu
CWID: 891461741
Project 1: Text in Image

HW1_encoder.py and HW1_decoder.py were developed and tested using Python 3.6 running on a Windows 10
machine.

The program uses an image's existing pixels to hide a secret message within the image.
By altering the last digit in the image's R, G, and B pixels I am able to hide a binary 1 or 0 
which when decoded will reveal a hidden binary string that is translatable to ASCII characters 
to reveal a message. Because I am altering the least significant bit in every pixel the changes 
in the image will be unnoticeable to the naked eye.

To run the program:
	* Both the image and the programs must be in the same directory.
	* You must have the Pillow module for Python.
	* Open Command Prompt or terminal and navigate to the directory the image and program are in. 
	* Once in the directory, run HW1_encoder.py to encrypt a message in the image.
	* HW1_encoder.py will save an image with the hidden message to the working directory.
	* To decode the message, run HW1_decoder.py
	* The secret message encoded in HW1_encoder.py will be displayed in the terminal.