from pushbullet import Pushbullet
pb = Pushbullet("o.xWndImaQeTc7WvQC6tK3yyTAJVdBKxrU")
push = pb.push_note("Title","body")

print(pb.devices)

samsung = pb.get_device('Samsung SM-G950F')
push = samsung.push_note("Message","Test message")
push = samsung.push_note('type': 'IMAGE_MESSAGE', 'filePath': /home/pi/Desktop/bmc.png, 'bmc.png')
