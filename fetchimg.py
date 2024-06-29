import os
import time
name=time.time()
os.system("mkdir "+str(name))
while(True):
    os.system("pscp -pw <INSERT_PASSWORD_HERE> arg@raspberrypi:/home/arg/image.jpg ./"+str(name)+"/image"+str(time.time())+".jpg")
    time.sleep(60)
