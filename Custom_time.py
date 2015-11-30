# This is the test program for the PI GPO


import time
import sys
import signal
import threading

	

class Timer:
	def __init__(self, start_time=0,format="s", handle_enable="n"):
		self.at=0
		self.st= start_time
		self.dt=0
		self.s = False
		self.format=format
		#org_sig_hand = signal.getsignal(signal.SIGINT)
		if handle_enable == "y":
			signal.signal(signal.SIGINT, self.__Timer_handle)
			self.__toggle =True
		elif handle_enable =="n":
			signal.signal(signal.SIGINT, signal.SIG_DFL)			
	def start(self):
		self.at=time.time()
	def lap(self):
		if self.s== False:
			self.dt=time.time()-self.at+self.st
		
		if self.format == "m":	
			return self.dt*10**3
		else:
			return self.dt
	def reset(self,start_time=0):
		self.dt=0
		self.st=start_time
	def stop(self):
		self.dt=time.time()-self.at+self.st
		self.st = self.dt
		self.s= True
	def __Timer_handle(self,signum,frame):
		if self.__toggle == True:
			self.start()
			self.__toggle=False
		elif self.__toggle == False:
			self.stop()
			self.__toggle=True
		
		
		


if __name__ == ("__main__"):

	try:		
		T1 = Timer(3,"m")
		T1.start()
		while T1.lap()<20:
			print T1.lap()	
	except:
		raise
		
		 		
	

