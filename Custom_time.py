# This is the test program for signal amd threading class


import time
import sys
import signal
import threading
import os
import copy

	

class Timer(object):
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
		
class Timeout(threading.Thread):
	def __init__(self,end_time=0,start_time=0,format='s',target=None, name=None, group=None,*args,**kwargs):
		super(Timeout,self).__init__(name=name, target=target,group=group,*args,**kwargs) 
	#threading.Thread has the following __init__ function
	#def __init__(self, group=None, target=None, name=None,
    #args=(), kwargs=None, verbose=None)
		self.et=end_time
		if format != 'm' and format !='s':
			sys.exit("AttributeError: format only accepts 's' for seconds or 'm' for milli seconds")
		self.timer=Timer(start_time=start_time,format=format)
		self.__kill=0
	def __str__(self):
			if self.timer.format is's':
				unit = "s"
			else:
				unit = "ms"
			return ("name:{0}\nstart_time:{1}\nend_time:{2}{3}".format(self.name,self.timer.st,self.et, unit))		
	def run(self):
			self.timer.start()
			while(self.timer.lap()<self.et and self.__kill==0):
				pass
			if self.__kill==1:	
				self.__kill=0
			elif self.__kill==0:
				os.kill(os.getpid(), signal.SIGUSR1)
	def reset(self,end_time=None):
			self.__kill=1
			self.timer.reset()
			if end_time is not None:
				self.et=end_time

def start(T):
	if not T.is_alive():
		temp = Timeout()
		temp.et = T.et
		temp.timer=T.timer
		T = temp
		T.start()
		print T.is_alive()
	else:
		raise Exception("Timer is already running. You should reset it before running another one")

def reset(T):
	T.reset()
	#T.join()
				
				
				
def SIGUSR1_handle(signum, frame):
	raise Exception("Timeout")

		

if __name__ == '__main__':
	
	
	 signal.signal(signal.SIGUSR1,SIGUSR1_handle)
	 T2 = Timeout(end_time=2,format='m')
	 T1 = Timer()
	 print T2
	 start(T2)
	 T1.start()
	 try:
		 while T1.lap()<10:
			if T1.lap()>1:
				reset(T2)
			print T1.lap()
			T1.reset()
	 except Exception as e:
		T1.reset()
		pass
	 finally:
		 print "done 1"
		 
	 print T2.is_alive()	
	 start(T2)
	 print T2.is_alive()	
	 reset(T2)
	 print T2.is_alive()	
	 
	 T1.start()
	 try:
		 while T1.lap()<10:
			if T1.lap()>10:
				T2.reset()
			print T1.lap()
			T1.reset()
	 except Exception as e:
		pass
	 finally:
		 print "done 2"
	 #time.sleep(10)
		 		
	

