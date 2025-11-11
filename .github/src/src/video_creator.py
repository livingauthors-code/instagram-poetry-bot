import os
import random
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
from config import Config

class VideoCreator:
    def __init__(self):
        pass
    
    def create_poetry_video(self, audio_file, text, author, title, output_file):
        try:
            background = self._get_random_background()
            if not background:
                # Если нет фона, создадим черный фон
                from moviepy.editor import ColorClip
                video_clip = ColorClip(size=Config.VIDEO_RESOLUTION, color=(0,0,0), duration=10)
            else:
                video_clip = VideoFileClip(background).subclip(0, 10)
            
            audio_clip = AudioFileClip(audio_file)
            video_clip = video_clip.set_audio(audio_clip).set_duration(audio_clip.duration)
            
            # Текст
            title_clip = TextClip(f"{title}\n{author}", fontsize=40, color='white', 
                                stroke_color='black', stroke_width=2).set_duration(audio_clip.duration).set_position(('center', 'top'))
            text_clip = TextClip(text, fontsize=30, color='white', 
                               stroke_color='black', stroke_width=1).set_duration(audio_clip.duration).set_position('center')
            
            final_video = CompositeVideoClip([video_clip, title_clip, text_clip])
            final_video.write_videofile(output_file, fps=24, verbose=False, logger=None)
            
            return True
            
        except Exception as e:
            print(f"Ошибка при создании видео: {e}")
            return False
    
    def _get_random_background(self):
        backgrounds = []
        for file in os.listdir(Config.BACKGROUNDS_DIR):
            if file.lower().endswith(('.mp4', '.mov', '.avi')):
                backgrounds.append(os.path.join(Config.BACKGROUNDS_DIR, file))
        
        return random.choice(backgrounds) if backgrounds else None
