import os

class Config:
    BACKGROUNDS_DIR = "assets/backgrounds"
    FONTS_DIR = "assets/fonts"
    MUSIC_DIR = "assets/music"
    OUTPUT_DIR = "output"
    AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
    VIDEO_DIR = os.path.join(OUTPUT_DIR, "videos")
    DATA_DIR = "data"
    
    POEMS_CSV = os.path.join(DATA_DIR, "poems.csv")
    POSTED_POEMS_FILE = os.path.join(DATA_DIR, "posted_poems.txt")
    
    VIDEO_RESOLUTION = (1080, 1920)
    VIDEO_FPS = 24
    BACKGROUND_MUSIC_VOLUME = 0.1
    
    FONT_PRIMARY = os.path.join(FONTS_DIR, "arial.ttf")
    FONT_BOLD = os.path.join(FONTS_DIR, "arialbd.ttf")
    TEXT_COLOR = "white"
    TEXT_STROKE_COLOR = "black"
    TEXT_STROKE_WIDTH = 2
    
    MAX_CAPTION_LENGTH = 2200
    HASHTAGS = [
        "#поэзия", "#стихи", "#литература", "#поэты", "#русскаяпоэзия",
        "#классика", "#чтение", "#искусство"
    ]

for directory in [Config.BACKGROUNDS_DIR, Config.FONTS_DIR, Config.MUSIC_DIR,
                  Config.AUDIO_DIR, Config.VIDEO_DIR, Config.DATA_DIR]:
    os.makedirs(directory, exist_ok=True)
