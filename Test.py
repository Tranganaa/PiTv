import sys
import signal
from PIgpo import Quad
from PIgpo import timer

t = timer(3)
j=0
def INTtest(signum, frame):
	global j
	if j==0:
		t.start()
		j=1
		pass
	else:
		t.clear()
		j=0
		pass

signal.signal(signal.SIGINT, INTtest)

print "Area is {}".format(Quad(2,3).area())


try:
	i=0
	while True:
		i+=1
		print "%i"%i
except KeyboardInterrupt:
	pass	
except:
	raise


	
	

