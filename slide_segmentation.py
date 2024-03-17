from moviepy.editor import *
import pandas as pd
import os
import imageio
import json
import time
import yt_dlp
import re
from os.path import isfile, join, isdir
from IPython.display import clear_output

"""# Load data"""

# Load the CSV file into a DataFrame
links = pd.read_csv('/content/lecture_vids.csv')

# Iterate over the rows of the DataFrame and download videos using yt-dlp
for index, row in links.iloc[:].iterrows():  # Start from the 12th row
    video_link = row['link']
    !yt-dlp -o '/content/drive/MyDrive/ColabNotebooks/%(playlist)s/%(playlist_index)s. %(title)s.%(ext)s' {video_link}

def extract_playlist_titles(playlist_url):
    ydl_opts = {
        "extract_flat": True,  # Flatten the playlist
        "get_title": True,  # Get the title of each video
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        # Extract the titles and their order
        titles = [entry["title"] for entry in result["entries"]]
    return titles


# URL of the YouTube playlist
playlist_url = (
    "https://www.youtube.com/playlist?list=PLM3o01n9O7-C8CC-W_qi2o9yYSsKIXUE9"
)

# Extract video titles and their order from the playlist
titles = extract_playlist_titles(playlist_url)

"""# Frame Extraction"""

from tqdm.autonotebook import tqdm


def extract_frames(video_path, output_folder, segment, key):
    # Load the video
    video = VideoFileClip(video_path)
    # Extract frames at specified intervals
    try:
        for i in tqdm(range(len(segment))):
            # Calculate the time to extract frame
            time_to_extract = int(segment.values[i] - 1)

            # Extract the frame at the specified time
            frame = video.get_frame(time_to_extract)
            # Save the frame as an image
            output_path = join(output_folder, f"{key}_frame_{i}.png")
            imageio.imwrite(output_path, frame)
    except Exception as e:
        return False
    # Close the video file
    video.close()
    return True

def extract(DIR):

    # Load the CSV file into a DataFrame
    list_folder = sorted(os.listdir(join(DIR, "videos")))

    segments = []
    for path in sorted(os.listdir(join(DIR, "segments"))):
        # Check if path is folder
        dir = join(DIR, "segments", path)
        if "ipynb" in path:
            continue
        if isdir(dir):
            segments.append(
                pd.read_csv(join(dir, "segments.txt"), header=None, names=[f"{path}"])
            )

    # Create a folder to store the extracted images
    output_folder = join(DIR, "image_extraction")
    os.makedirs(output_folder, exist_ok=True)

    # Extract frames from the video
    idx_to_pop = []
    for idx, segment in enumerate(segments):
        key = segment.keys()[0]
        # if key in exists:
        vid_path = None
        tqdm.write(key)
        for i in list_folder:
            if (key + ". ") in i:
                vid_path = join(DIR, "videos", i)
                break

        if not vid_path:
            # segments.pop(idx)
            idx_to_pop += [key]
            continue
        tqdm.write(vid_path)
        res = extract_frames(vid_path, output_folder, segment, key)
        if not res:
            tqdm.write("Failed")
            idx_to_pop += [key]

    # Get the spoken texts
    spoken_texts = {}
    count = 0
    keys = [segment.keys()[0] for segment in segments]
    for keys in tqdm(keys):
        if keys in idx_to_pop:
            continue
        tmp = {}
        for i, path in enumerate(sorted(os.listdir(join(DIR, "segments", keys)))):
            source = {}
            if "spoken" in path:
                slide_num = int(path.split("_")[1])
                tmp[slide_num] = {}
                df = pd.read_csv(join(DIR, "segments", keys, path))
                tmp[slide_num][f"path_slide"] = join(
                    DIR, "image_extraction", f"{keys}_frame_{slide_num}.png"
                )
                tmp[slide_num][f"slide_source"] = " ".join(map(str, df["Word"].values))
        spoken_texts[keys] = tmp

    # Save the spoken texts to a JSON file
    with open(join(DIR, "spoken_texts.json"), "w") as f:
        json.dump(spoken_texts, f)

DIR = "Slide-data/psy-1" # Change with subject paths
for i in os.listdir(DIR):
    if isdir(join(DIR, i)):
        extract(join(DIR, i))
    clear_output()