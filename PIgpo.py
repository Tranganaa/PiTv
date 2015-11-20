# This is the test program for the PI GPO


import time
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!")

#Initital Setup
inPin = 18 #Our primary input channel

GPIO.setmode(GPIO.BCM) #Boradcom pin-numbering scheme
print "mode {0}\n".format(GPIO.getmode()) #Check the pin-numbering mode

GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
input=GPIO.input(inPin)
try:
	while True:
		print("%i\n")%GPIO.input(inPin)
		if input ==0:
			print("Signal Recieved")
			break
except KeyboardInterrupt:
	raise	




#try:
#	while i<20:
#		print "i=%i\n"%i
#		time.sleep(1) #wait for 10 ms
#		i+=1
#		
#except KeyboardInterrupt:
#	raise	
#except:
#	print("Someother Error\n")
