# Multimodal Lecture Presentations Dataset

# Requirements

Để được kết quả bao gồm image + text. Ta cần dữ liệu phải có những phần sau:
1. Video (Online/Offline)
2. Segment (Thời gian chuyển tiếp giữa các slide)
3. Spoken Text (Lời thoại trong video)
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

# Preprocess 

1. Load dữ liệu về từ youtube (theo bộ dataset đang sử dụng) - bao gồm cả video và title.
2. So sánh dữ liệu thu thập được với folder của dataset (do dữ liệu tải về sẵn không khớp với dữ liệu từ youtube) và chọn lọc ra những phần chung.
3. Đọc file segment của từng folder (tức từng video), gộp tất cả lại thành segments (biến này chứa tất cả segment file dưới dạng list(dataframe))
4. Viết lại *paths* cho video vì có những video không có folder data (tính năng dùng ocr để check đang được phát triển, nguyên nhân do folder và video title không trùng với nhau).
5. Cắt ảnh từ video dựa trên segments. 
6. Trích xuất lời thoại từ file *.csv* đóng gói thành file **spoken_texts.json** với format (path_slide + slide_source)
Ví dụ : 

```json
{
    "01": {
        "0": {
            "path_slide": "Slide-data/dental/Cariology/image_extraction/01_frame_0.png",
            "slide_source": "hey guys it's ryan at this video series will be on the science of cavities and i'm really excited to do this video i looked at a lot of current literature i'll try to make this stuff is interesting as possible i think it can be a little bit boring but i'm gonna do my best and we'll talk about the science behind how cavities are formed and then how that's relevant to our daily lives so it'll be a three part series"
        }
    }
}