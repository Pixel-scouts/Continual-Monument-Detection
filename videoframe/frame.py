from moviepy.editor import *
from moviepy.editor import VideoFileClip
from PIL import Image
import os

clip = VideoFileClip(r"D:\Major\videoframe\VID20230626113856.mp4")

fps = clip.fps
frame_rate = 10
frame_skip = round(fps / frame_rate)
frame_count = 0

for frame in clip.iter_frames():
    if frame_count % frame_skip == 0:
        frame_file = os.path.join("frame/", f"frame_{frame_count}.png")
        with open(frame_file, "wb") as f:
            # f.write(frame)
            Image.fromarray(frame).save(f, format='png')
    frame_count += 1


clip.reader.close()
clip.audio.reader.close_proc()