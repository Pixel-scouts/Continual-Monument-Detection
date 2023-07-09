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

# Custom ArgumentParser for custom error message
class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f"{message}")
        print("Use --help for available options.")
        self.exit(2)



def extract_frames(video_path, output_dir):
    """
    Extaracts frames from the given video file and saves to output directory.
    
    Parameters:
    - Videos_path (String): Path to Video file to extract frames from
    - output_dir (String): Path to folder to save extracted frames
    """

    # create output Directory if not present
    os.makedirs(output_dir, exist_ok=True)
    # create handler for Video
    cap = cv2.VideoCapture(video_path)
    # get the fps from video
    fps = cap.get(cv2.CAP_PROP_FPS)
    # set number of frames to save per second
    frame_rate = 10
    # get the nth frame to save, others are discarded
    frame_save = round(fps / frame_rate)
    frame_count = 0

    while True:
        is_read, frame = cap.read()
        # get the base name of video file
        filename = os.path.splitext(os.path.basename(video_path))[0]
        # if the next frame isn't read i.e end of frames exit loop
        if not is_read:
            break
        # save frames matching the condition
        if frame_count % frame_save == 0:
            # orientation=cap.get(cv2.CAP_PROP_ORIENTATION_META)
            # print(orientation)
            frame_file = os.path.join(output_dir, f"{filename}_frame_{frame_count}.jpg")
            cv2.imwrite(frame_file, frame)
        frame_count += 1
    

if __name__ == "__main__":
    parser = CustomArgumentParser(prog='Frame',description="Extract frames from a videos")
    parser.add_argument("-v", "--video", type=str, help="Path to the video file")
    parser.add_argument("-o", "--output", type=str, help="Path to the output directory")
    args = parser.parse_args()
    video_path = args.video
    output_dir = args.output

    extract_frames(video_path, output_dir)