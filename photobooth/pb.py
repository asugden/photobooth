import os, subprocess, time, random



def getPhotos():
	global path
	files = os.listdir(path)
	out = []
	for file in files:
		if file.find('IMG') > -1 and file.find('.JPG') > -1:
			out.append(file)
	return out

def waitForButton(con):
	response = con.read()
	print (response)
	if response == '1':
		subprocess.check_output('open -a /Users/arthur/Documents/Programs/Photobooth-all-computer/new/takephoto.app', shell=True)
		waitForButton(con)
	if response == '2':
		print ("Beginning alignment...")
		global path
		subprocess.check_output('open -a /Users/arthur/Documents/Programs/Photobooth-all-computer/new/takephoto.app', shell=True)
		print (subprocess.check_output('open -a /Users/arthur/Documents/Programs/Photobooth-all-computer/new/takephoto.app', shell=True))
		time.sleep(5)
		str = 'convert '
		files = getPhotos()
		if len(files) > 0:
			for file in files:
				str = str + path + file + ' '
			str = str + '+append -border 5 ' + path + 'test.jpg'
			print ("Combining files")
			print (str)
			print (subprocess.check_output(str, shell=True))
			print ('bam')

def randomPhrase():
	phrases = [
		'work it',
		'smile harder',
		'feel the burn',
		'say shit',
		'strike a pose',
		'bop it',
		'hot stuff',
		'you look pretty',
		'say cheese',
		'why the face?',
		'look out',
		'behind you',
		'psych',
		'wait for it',
		'friendsgiving!',
		'photo bomb',
		'flash',
		'give mike a squeeze',
		'wave your hands in the air',
		'thats what I\'m talking about',
		'shake what your momma gave you',
		'dont stop till you get enough',
		'oh baby',
	]

	os.system('say '+random.choice(phrases))

def photoprint(path):
	os.system('lp -d "Canon_CP910" -o media="Postcard(4x6in)_Type2" %s' % (path)) 

def photomerge(names):
	print ("Beginning alignment...")

	tname = time.strftime("%H-%M-%S", time.gmtime())
	for i, n in enumerate(names):
		os.system('convert %s -resize 800x1200 -bordercolor white -border 12 %i.jpg' % (n, i))

	os.system('convert 1.jpg 0.jpg -append 01.jpg')
	os.system('convert 3.jpg 2.jpg -append 23.jpg')
	os.system('convert 01.jpg 23.jpg +append -bordercolor white -border 5 %s-comb.jpg' % (tname))

	return '%s-comb.jpg' % (tname)

#	convert \( image1 image2 -append \) \( image3 image4 -append \) +append result


def photograph(port):
	photoz = []

	for i in range(4):
		tname = time.strftime("%H-%M-%S", time.gmtime())
		photoz.append(tname+'.jpg')
		print (tname)
		os.system('say three')
		time.sleep(0.3)
		os.system('say two')
		time.sleep(0.5)
		os.system('say one')
#		time.sleep(0.5)

		if random.random() < 0.2:
			randomPhrase()
		# Get port with gphoto2 --auto-detect
		print( 'gphoto2 --port "%s" --camera "Canon EOS 5D Mark II" --capture-image-and-download --filename %s.jpg' % (port, tname))
		print (os.system('gphoto2 --port "%s" --capture-image-and-download --filename %s.jpg' % (port, tname)))

	save = photomerge(photoz)
	print ('photoprint', save)
	photoprint(save)

#		time.sleep(2)

def autodetectport(data):
	data = data.decode("utf-8").split('\n')[-2]
	data = data.strip()
	data = data.split(' ')
	data = data[-1]
	PORT = data
	print(PORT)
	return data


PORT = 'usb:002,002'

if __name__ == '__main__':
	import subprocess

#	photoprint('wolf-in-sheeps-clothing-fullsize-1.jpg')
	os.system('killall PTPCamera')
	portinfo = subprocess.check_output('gphoto2 --auto-detect', shell=True)
	port = autodetectport(portinfo)
	while True:
		t = subprocess.check_output('read -n1', shell=True)
		if t == 'q':
			exit(1)
		else:
			photograph(port)
