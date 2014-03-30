import subprocess
import os

file_list=["../videos/tomorrow.mp4",'../videos/i.mp4','../videos/eat.mp4','../videos/pizza.mp4']


f=open("list.tmp","w")
for i in file_list:
	f.write("file '"+ i +"'\n")
f.close()

os.system("ffmpeg -f concat -i list.tmp -c copy output.mp4")
os.remove('list.tmp')

