import sys,os
sys.path.append('/home/pi/MyProject/RPi.GPIO-0.1.0')

import blink
import time

for i in range(5):
    t=time.time()
    cmd= "raspistill -o ./pics/image"+str(i)+"_"+str(t)+".jpg"
    os.system(cmd)	
    iterations = 5
    speed = 0.3
    blink.Blink(int(iterations),float(speed))
    time.sleep(0.2)
print "done"
