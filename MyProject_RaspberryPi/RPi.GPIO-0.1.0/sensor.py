import RPi.GPIO as GPIO ## Import GPIO Library
import time ## Import 'time' library.  Allows us to use 'sleep'
import os

PIR_PIN=11
PIR_PIN_OUT=7
GPIO.setup(PIR_PIN,GPIO.IN)
GPIO.setup(PIR_PIN_OUT,GPIO.OUT)

def MOTION(SleepTime):
	print "Motion detected"
    	t=time.time()
	for i in xrange(2):
		print "first",i
        	GPIO.output(7, True) ## Turn on GPIO pin 7
        	time.sleep(0.5) ## Wait
        	GPIO.output(7, False) ## Switch off GPIO pin 7
		time.sleep(0.5)
    	cmd= "raspistill -o ./pics/image_"+str(t)+".jpg"
    	os.system(cmd)
	cmd = "/home/pi/MyProject/RasPiCamcorder-master/Dropbox-Uploader/dropbox_uploader.sh upload "+"./pics/image_"+str(t)+".jpg"+" pics/image_"+str(t)+".jpg"
	os.system(cmd)	
	for i in xrange(5):
		print "second",i
		GPIO.output(7, True) ## Turn on GPIO pin 7
        	time.sleep(0.5) ## Wait
        	GPIO.output(7, False) ## Switch off GPIO pin 7
		time.sleep(0.5)

print "ctrl+c to exit"
time.sleep(2)
print "ready"

try:
	#GPIO.add_event_detect(PIR_PIN,GPIO.RISING,callback=MOTION)
	c,a=0,0
	while 1:
		c+=1
		val=GPIO.input(PIR_PIN)
		if val:
			a+=1
			print val,a,"___________________"
			MOTION(.5)
			c=0
			time.sleep(2)
		
except KeyboardInterrupt:
 	print "QUIT"

