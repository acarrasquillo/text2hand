import subprocess

ffmpeg_command1 = ["ffmpeg", "-f", "concat", "-i", "video_list.txt", "-c", "copy","output.mp4"]

subprocess.call(ffmpeg_command1)