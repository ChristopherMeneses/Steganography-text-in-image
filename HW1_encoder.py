# Christopher Meneses
# chrismeneses@csu.fullerton.edu
# CWID 891461741
# CPSC 353 Section 02
# Project 1: Text In Image
# HW1_encoder.py

from PIL import Image

# Load image from the directory HW1.py is in.
# In my testing, all programs and images were on Desktop
original_im = Image.open("gastronome.jpeg")

# Get the image width and height, in pixels
width, height = original_im.size

# Convert the image into an RGB copy
rgb_im = original_im.convert('RGB')

# The message to hide in the image, as a string
hidden_message = "Hello"

# Get the length of the hidden message in the form of a string
message_length = str(len(hidden_message))

# Convert the message and its length to a list of binary values
binary_hidden_message = (list(map(bin, bytearray(hidden_message, 'utf8'))))
binary_msg_length = (list(map(bin, bytearray(message_length, 'utf8'))))

# Create an iterator for the coordinates of the pixels
height_it = height - 1
width_it = width - 1 
	
# We will need 2 pixels for each binary representation of a string
# 	character of a number, since they are at most 6 bits long, for
#	example: string 5 is represented as 110101
for y in binary_msg_length:
	r, g, b = rgb_im.getpixel((width_it, height_it))
	r_list = list(str(r))
	g_list = list(str(g))
	b_list = list(str(b))
	
	# Place a 1 or 0 in a list to transfer over to a pixel
	if y[2] == '1':
		r_list[len(r_list) - 1] = '1'
	elif y[2] == '0':
		r_list[len(r_list) - 1] = '0'
	if y[3] == '1':
		g_list[len(g_list) - 1] = '1'
	elif y[3] == '0':
		g_list[len(g_list) - 1] = '0'
	if y[4] == '1':
		b_list[len(b_list) - 1] = '1'
	elif y[4] == '0':
		b_list[len(b_list) - 1] = '0'
				
	# Join the lists into one onvertable string
	final_r = ''.join(r_list)
	final_g = ''.join(g_list)
	final_b = ''.join(b_list)
				
	# Convert to int
	final_r = int(final_r)
	final_g = int(final_g)
	final_b = int(final_b)
				
	r_list.clear()
	g_list.clear()
	b_list.clear()
				
	# Place into image
	original_im.putpixel((width_it, height_it), (final_r, final_g, final_b))
		
	width_it -= 1
		
	r, g, b = rgb_im.getpixel((width_it, height_it))
	r_list = list(str(r))
	g_list = list(str(g))
	b_list = list(str(b))
				
	if y[5] == '1':
		r_list[len(r_list) - 1] = '1'
	elif y[5] == '0':
		r_list[len(r_list) - 1] = '0'
	if y[6] == '1':
		g_list[len(g_list) - 1] = '1'
	elif y[6] == '0':
		g_list[len(g_list) - 1] = '0'
	if y[7] == '1':
		b_list[len(b_list) - 1] = '1'
	elif y[7] == '0':
		b_list[len(b_list) - 1] = '0'				
					
	# Join the lists into one onvertable string
	final_r = ''.join(r_list)
	final_g = ''.join(g_list)
	final_b = ''.join(b_list)
				
	# Convert to int
	final_r = int(final_r)
	final_g = int(final_g)
	final_b = int(final_b)
				
				
	# Place into image
	original_im.putpixel((width_it, height_it), (final_r, final_g, final_b))
				
	width_it -= 1
	
width_it = width - 12
		
for letter in binary_hidden_message:
	if width_it < 0:
		height_it -= 1
		width_it = width - 1

	# Print a message in case the message is too long to hide in the image
	#   and exit the program
	if height_it < 0:
		print("The message is too long to hide in this image")
		quit()
			
	r, g, b = rgb_im.getpixel((width_it, height_it))
	r_list = list(str(r))
	g_list = list(str(g))
	b_list = list(str(b))
	
	
	if letter[2] == '1':
		r_list[len(r_list) - 1] = '1'
	elif letter[2] == '0':
		r_list[len(r_list) - 1] = '0'
	if letter[3] == '1':
		g_list[len(g_list) - 1] = '1'
	elif letter[3] == '0':
		g_list[len(g_list) - 1] = '0'
	if letter[4] == '1':
		b_list[len(b_list) - 1] = '1'
	elif letter[4] == '0':
		b_list[len(b_list) - 1] = '0'
	
	# Join the lists into one onvertable string
	final_r = ''.join(r_list)
	final_g = ''.join(g_list)
	final_b = ''.join(b_list)
		
	# Convert to int
	final_r = int(final_r)
	final_g = int(final_g)
	final_b = int(final_b)
		
	r_list.clear()
	g_list.clear()
	b_list.clear()
			
	# Place into image
	original_im.putpixel((width_it, height_it), (final_r, final_g, final_b))

	width_it -= 1
			
	r, g, b = rgb_im.getpixel((width_it, height_it))
	r_list = list(str(r))
	g_list = list(str(g))
	b_list = list(str(b))
			
	if letter[5] == '1':
		r_list[len(r_list) - 1] = '1'
	elif letter[5] == '0':
		r_list[len(r_list) - 1] = '0'
	if letter[6] == '1':
		g_list[len(g_list) - 1] = '1'
	elif letter[6] == '0':
		g_list[len(g_list) - 1] = '0'
	if letter[7] == '1':
		b_list[len(b_list) - 1] = '1'
	elif letter[7] == '0':
		b_list[len(b_list) - 1] = '0'				
				
	# Join the lists into one onvertable string
	final_r = ''.join(r_list)
	final_g = ''.join(g_list)
	final_b = ''.join(b_list)
			
	# Convert to int
	final_r = int(final_r)
	final_g = int(final_g)
	final_b = int(final_b)
			
				
	# Place into image
	original_im.putpixel((width_it, height_it), (final_r, final_g, final_b))
	
	width_it -= 1
	
	r_list.clear()
		
	r, g, b = rgb_im.getpixel((width_it, height_it))
	r_list = list(str(r))
	
	if letter[8] == '0':
		r_list[len(r_list) - 1] = '0'
	elif letter[8] == '1':
		r_list[len(r_list) - 1] = '1'
			
	final_r = ''.join(r_list)
	final_r = int(final_r)
			
	original_im.putpixel((width_it, height_it), (final_r, g, b))
	
	width_it -= 1
	r_list.clear()
	g_list.clear()
	b_list.clear()

# save encoded image as a lossless .PNG in the working directory
original_im.save("final.png")