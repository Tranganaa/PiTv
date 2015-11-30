import sys
from PIgpo import Quad
from PIgpo import timer




print "Area is {}".format(Quad(2,3).area())


try:
	timer(3).start()
	i=0
	while True:
		i+=1
		print "%i"%i
except KeyboardInterrupt:
	timer.clear()
except:
	print "Interrupt Occured"



	
	

