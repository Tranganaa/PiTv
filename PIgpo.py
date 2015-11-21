# This is the test program for the PI GPO


import time
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!")

#Initital Setup
inPin = 18 #Our primary input channel
testPin	=17		

GPIO.setmode(GPIO.BCM) #Boradcom pin-numbering scheme
print "mode {0}\n".format(GPIO.getmode()) #Check the pin-numbering mode

GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(testPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
class RC:
	def _init_(self):
		self.code = int('0000000000000',2)
		self.command = self.__command(self.code)
		self.address = self.__address(self.code)
	def update(self,Pin):
		self.code = self.__process(Pin)
		self.address = self.__address(self.code)
		self.command = self.__command(self.code)
	def __command(self,code):
		return self.code & int('111111',2)
	def __address(self,code):
		return self.code & int('11111000000',2)>>6
	#def __process(self,Pin):
		

t=[]
tdiff=[] 
val =[]
try:
	#for i in range(0,40):
	#	GPIO.wait_for_edge(inPin, GPIO.FALLING)
	#	t.append(time.time())
	#	GPIO.wait_for_edge(inPin, GPIO.RISING)
	#	t.append(time.time())
	#	tdiff.append(t[2*i+1]-t[2*i])
	#print tdiff
	GPIO.wait_for_edge(inPin, GPIO.FALLING)
	t2=0	
	while (t2<0.5):
		val.append(GPIO.input(inPin))
		time.sleep(0.002)
		t2 +=0.002
	print "\n"
	print val		 
#	while True:
#		input=GPIO.input(inPin) #GPIO.input(testPin)] 
#		print'{0}\n'.format(input)
#		if input == 0:
#			print("Signal Recieved")
#			break
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
