from moviepy.editor import VideoFileClip
from PIL import Image
import os
import argparse
parser = argparse.ArgumentParser(description="Extract frames from a video")
parser.add_argument("-v", "--video", type=str, help="Path to the video file")
parser.add_argument("-o", "--output", type=str, help="Path to the output directory")
args = parser.parse_args()

def extract_frames(video_path, output_dir):
    clip = VideoFileClip(video_path)

    fps = clip.fps
    frame_rate = 10
    frame_skip = round(fps / frame_rate)
    frame_count = 0

    print(video_path)
    print(output_dir)

    for frame in clip.iter_frames():
        if frame_count % frame_skip == 0:
            frame_file = os.path.join(output_dir, f"frame{frame_count}.jpg")
            with open(frame_file, "wb") as f:
                Image.fromarray(frame).save(f, format='JPEG')
        frame_count += 1

    clip.reader.close()
    clip.audio.reader.close_proc()

if __name__ == "__main__":
    video_path = args.video
    output_dir = args.output

    extract_frames(video_path, output_dir)