from moviepy.editor import VideoFileClip
from PIL import Image
import cv2
import numpy as np
import os
import argparse
parser = argparse.ArgumentParser(description="Extract frames from a video")
parser.add_argument("-v", "--video", type=str, help="Path to the video file")
parser.add_argument("-o", "--output", type=str, help="Path to the output directory")
args = parser.parse_args()


def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    # orientation = get_video_orientation(video_path)
    cap = cv2.VideoCapture(video_path)
    # clip = VideoFileClip(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_rate = 10
    frame_save = round(fps / frame_rate)
    frame_count = 0

    print(video_path)
    print(output_dir)

    while True:
        is_read, frame = cap.read()
        filename = os.path.splitext(os.path.basename(video_path))[0]
        if not is_read:
            break
        if frame_count % frame_save == 0:
            # orientation=cap.get(cv2.CAP_PROP_ORIENTATION_META)
            # print(orientation)
            frame_file = os.path.join(output_dir, f"{filename}_frame_{frame_count}.jpg")
            print(frame_file)
            cv2.imwrite(frame_file, frame)
            break
        frame_count += 1
    

if __name__ == "__main__":
    video_path = args.video
    output_dir = args.output

    extract_frames(video_path, output_dir)