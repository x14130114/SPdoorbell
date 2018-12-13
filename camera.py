from picamera import PiCamera
from time import sleep
from datetime import datetime
from grovepi import *
import grovepi
import time
import sys
from pushbullet import Pushbullet
#from pushbullet2 import PushBullet

#connecting to pusb bullet api
pb = Pushbullet("o.xWndImaQeTc7WvQC6tK3yyTAJVdBKxrU")
pushes = pb.get_pushes()
print(pushes)

print(pb.devices)
samsung = pb.get_device('Samsung SM-G950F')

button = 7
ultrasonic_ranger = 2
grovepi.pinMode(button,"INPUT")
camera = PiCamera()
now = datetime.now()
filename = ''

print grovepi.ultrasonicRead(ultrasonic_ranger)

def take_photo():
	global filename
	#change this naming convention as it is not working
	filename = 'bell.jpg'
	camera.resolution = (1280, 960)
	camera.rotation = 180
	camera.start_preview()
	sleep(1)
	camera.capture('/home/pi/Desktop/Bmc/pb/' + (filename))
	camera.stop_preview
	push_notification()
	#sys.exit()

#when button is pressed, send_push notification to phone via pushbullet api	
def push_notification():
	print 'sending push notification with image...'
	with open("bell.jpg", "rb") as pic:
		img = pb.upload_file(pic, "Visitor at the door")
	push = samsung.push_file(**img)
	#push1 = pb.push_file(file_url="/home/pi/Desktop/Bmc/pb/bell.jpg", file_name="bell.jpg", file_type="image/jpeg")
	#push1 = samsung.push_note("Doorbell Alert","Visitor at the door..")
	print 'sent........'

##ultrasonic range within 20cm take pic and store it on RPi
def ultra():
	global filename1
	#change this naming convention as it is not working
	filename1 = 'ultra.png'
	print 'starting resolution...'
	camera.resolution = (2592, 1944)
	print 'starting rotation...'
	camera.rotation = 180
	print 'starting preview...'
	camera.start_preview()
	sleep(1)
	print 'starting capture...'
	print ('/home/pi/Desktop/Bmc/pb/'+ (filename1))
	camera.capture('/home/pi/Desktop/Bmc/pb/'+ (filename1))
	print 'stopping preview...'
	camera.stop_preview
	
while True:
    try:
        print(grovepi.digitalRead(button))
        time.sleep(.5)
	if grovepi.digitalRead(button) == 1:
		take_photo()
	elif grovepi.ultrasonicRead(ultrasonic_ranger) < 20:
		ultra()
    except IOError:
        print ("Error")


#pbullet = samsung.push('IMAGE_MESSAGE', /home/pi/Desktop/bmc.png)
#push = pb.push_note("Title","body")
#pb.pushFile(devices[1]["Samsung SM-G950F"], "Intruder Alert!", "Image From PiCam", open(fileName, "bell.png"))
#push = pb.pushNote(devices[1]["iden"], 'Hello world', 'Test body')
