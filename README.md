# Multimodal Lecture Presentations Dataset
For more information about this dataset, please visit: [Multimodal Lecture Presentations Dataset:Understanding Multimodality in Educational Slides](https://github.com/dondongwon/LPMDataset) for more details. In this repository, I mainly mention the processing of the above data set to suit my intended use, specifically the task of generating slide based on paragraph to help lecture save time of making presentation slides.

# Requirements
To get image + text. We need data to have the following parts:
1. Video (Online/Offline)
2. Segment (Transition time between slides)
3. Spoken Text (Dialogue in the video)



# Preprocess 
Via this [link](https://drive.google.com/file/d/1n0ziL8Vd8GBC9B981dGA3cHfsm68S93R/view?usp=drive_link) to know more about my data processing.

## Step 
1. Load data from YouTube (according to the dataset being used) - including video and title.
2. Compare the collected data with the dataset folder (because the downloaded data does not match the data from YouTube) and select common parts.
3. Read the segment file of each folder (ie each video), combine them all into segments (this variable contains all segment files in the form of list(dataframe))
4. Rewrite *paths* for videos because there are videos that do not have folder data (the feature of using ocr to check is being developed, the reason is because the folder and video title do not match).
5. Crop images from videos based on segments.
6. Extract speech from *.csv* file and package it into **spoken_texts.json** file with format (path_slide + slide_source)
For example :
```json
{
    "01": {
        "0": {
            "path_slide": "Slide-data/dental/Cariology/image_extraction/01_frame_0.png",
            "slide_source": "hey guys it's ryan at this video series will be on the science of cavities and i'm really excited to do this video i looked at a lot of current literature i'll try to make this stuff is interesting as possible i think it can be a little bit boring but i'm gonna do my best and we'll talk about the science behind how cavities are formed and then how that's relevant to our daily lives so it'll be a three part series"
        }
    }
}
```
## Dataset Structure 
```bash
📂 ./
┗━━ 📂 Slide-data
    ┣━━ 📂 bio-3
    ┃   ┗━━ 📂 Biol1020
    ┃       ┣━━ 📂 segments
    ┃       ┃   ┣━━ 📂 01
    ┃       ┃   ┣━━ 📂 02
    ┃       ┃   ┣━━ 📂 03
    ┃       ┃   ┣━━ 📂 05
    ┃       ┃   ┣━━ 📂 07
    ┃       ┃   ┣━━ 📂 08
    ┃       ┃   ┣━━ 📂 09
    ┃       ┃   ┣━━ 📂 10
    ┃       ┃   ┣━━ 📂 13
    ┃       ┃   ┣━━ 📂 19
    ┃       ┃   ┗━━ 📂 22
    ┃       ┗━━ 📂 videos
    ┣━━ 📂 dental
    ┣━━ 📂 ml-1
    ┣━━ 📂 psy-1
    ┣━━ 📂 psy-2
    ┗━━ 📂 speaking
```
Via this [link](https://drive.google.com/drive/folders/17BphAsSj1WGiZC81_mxsxukFOVohhvhp?usp=drive_link) to download my processed data. 

