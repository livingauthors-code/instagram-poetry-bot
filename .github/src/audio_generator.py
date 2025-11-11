import os
from gtts import gTTS
import tempfile
from pydub import AudioSegment
from pydub.effects import normalize
from config import Config

class AudioGenerator:
    def __init__(self):
        pass
    
    def text_to_speech(self, text, output_file):
        try:
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                temp_path = temp_file.name
            
            tts = gTTS(text=text, lang='ru', slow=False)
            tts.save(temp_path)
            
            audio = AudioSegment.from_mp3(temp_path)
            audio = normalize(audio)
            audio.export(output_file, format="mp3", bitrate="192k")
            
            os.unlink(temp_path)
            return True
            
        except Exception as e:
            print(f"Ошибка при генерации аудио: {e}")
            return False
