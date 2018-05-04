# Christopher Meneses
# chrismeneses@csu.fullerton.edu
# CWID 891461741
# CPSC 353 Section 02
# Project 1: Text In Image
# HW1_decoder.py

from PIL import Image

# toString function was found on stackoverflow.com
# Credit goes to function creator who goes by user name 'user6320679'
def toString(binaryString):
    return "".join([chr(int(binaryString[i:i+8],2)) for i in range(0,len(binaryString),8)])

# Open the encoded image
original_im = Image.open("final.png")

# Get the image height and width, in pixels
width, height = original_im.size

# Convert the image into an RGB copoy
rgb_im = original_im.convert('RGB')

# Create an iterator for the coordinates of a pixel
width_it = width - 1
height_it = height - 1

# Create an iterator for when getting the message size. We know it will not
#   be longer than 11 pixels because it was given in the assignment specifications
msg_size_it = 11

# Create lists to hold out binary bits of data, data length, and our message
msg_length = list()
hidden_msg = list()
hidden_msg_bits = list()
msg_length_bits = list()

# A boolean to break out of the function if we do not use all 11 pixels for the 
#   message length
msg_length_over = False

# Get the size of the hidden message
while msg_size_it > 0:
	
	# We know that it takes 2 pixel's worth of values to extract a number, so we
	#   iterate through two sets of RGB's
	for x in range (0, 2):
		
		# Get the RGB values from a pixel with the specified coordinates
		r, g, b = rgb_im.getpixel((width_it, height_it))
		r_list = list(str(r))
		g_list = list(str(g))
		b_list = list(str(b))
		
		# Move to the next pixel
		width_it -= 1
		
		# Break from the loop if the pixel is not ecoded with a binary digit
		if r_list[len(r_list) - 1] != '0' or r_list[len(r_list) - 1] != '1':
			msg_length_over = True
		
		# Add binary digits to list
		msg_length_bits.append(r_list[len(r_list) - 1])
		msg_length_bits.append(g_list[len(g_list) - 1])
		msg_length_bits.append(b_list[len(b_list) - 1])
		
		# Clear the lists of RGB values
		r_list.clear()
		g_list.clear()
		b_list.clear()
		
		msg_size_it -= 1
	
	# Join and add the binary number to a list containing the length
	to_translate = ''.join(msg_length_bits)
	msg_length.append(toString(to_translate))
	
	
	if msg_length_over == True:
		break

# Join the message length list
msg_length = ''.join(msg_length)

# Set the message length
int_msg_length = int(msg_length)

# Set the width iterator just past the given 11 pixels for thet message length
width_it = width - 12

# Iterate through the pixels from bottom right to top left for the decrypted
#   message length
while int_msg_length > 0:	

	# Same as with digits, but we know that an ASCII character s 2 and 1/3 pixel
	#   RGB values
	for x in range (0, 3):
		
		# Get the RGB values at the pixel's given coordinates and place them in lists
		r, g, b = rgb_im.getpixel((width_it, height_it))
		r_list = list(str(r))
		g_list = list(str(g))
		b_list = list(str(b))
		
		# Add the values to a list holding all bits
		hidden_msg_bits.append(r_list[len(r_list) - 1])
		
		# Since we only use the third pixel's R value, we don't get the G or B value
		if x != 2:
			hidden_msg_bits.append(g_list[len(g_list) - 1])
			hidden_msg_bits.append(b_list[len(b_list) - 1])
		
		# Clear the lists
		r_list.clear()
		g_list.clear()
		b_list.clear()
		
		# Move to the next pixel
		width_it -= 1
		
		# Check to see if we have passed the leftmost pixel in a row and move to the
		#   next row if so
		if width_it < 0:
			height_it -= 1
			width_it = width - 1
	
	# Decrease the length iterator
	int_msg_length -= 1
	
	# Join the bits
	msg_to_translate = ''.join(hidden_msg_bits)
	hidden_msg_bits.clear()
	
	# Convert the binary number to ASCII and place it in a list
	hidden_msg.append(toString(msg_to_translate))

# Join the contents of the list holding the decrypted characters and print the message
print(''.join(hidden_msg))