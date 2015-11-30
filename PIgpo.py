# This is the test program for the PI GPO


import time
import sys
import signal
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
	def __init__(self):
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
class Quad:
	def __init__(self,w,l):
		self.width=w
		self.length=l
	def area(self):
		return (self.width*self.length)


class timer:
	def __init__(self,sec):
		self.sec=sec
	def start(self):
		signal.signal(signal.SIGALRM,self.timeout)
		signal.alarm(self.sec)
	def clear(self):
		signal.alarm(0)
	def timeout(self):
		pass

		
		
def comp(num,base,TOL):
	if abs(num-base)<TOL:
		return True
	else:
		return False

def sigINT_handler(signum, frame):
	print"Length of tdiff = {0}".format(len(tdiff))


if __name__ == '__main__':


	signal.signal(signal.SIGINT,sigINT_handler)	

	t=[]
	tdiff=[] 
	N=20
	val =[0]*N
	count=0
	i=0;

	GPIO.wait_for_edge(inPin, GPIO.FALLING)
	t.append(time.time())
	try:		
		while True:
			timer(0.01).start()
			GPIO.wait_for_edge(inPin, GPIO.FALLING)
			timer.clear()
			t.append(time.time())
			tdiff.append(t[i+1]-t[i])
			i+=1
	except:
		pass

	for i in range(0,N):
		if comp(tdiff[i],0.001,0.0003):
			val[i]=1
		elif comp(tdiff[i],0.002,0.0004):
			val[i]=0
		else:
			val[i]=2	
		print"{0:.3f} => {1}".format(tdiff[i],val[i])
		count+=1	
	
	
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
