import time
import os

file_list=["../videos/tomorrow.mp4",'../videos/i.mp4','../videos/eat.mp4','../videos/bacon.mp4']

def makeVideo(file_list):

	f=open("list.tmp","w")
	for i in file_list:
		f.write("file '"+ i +"'\n")
	f.close()
	name = str(time.time())
	os.system("ffmpeg -f concat -i list.tmp -c copy ./static/%s.mp4" % name)
	os.remove('list.tmp')
	return name +'.mp4'