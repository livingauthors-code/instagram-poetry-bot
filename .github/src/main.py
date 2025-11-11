import os
import time
from config import Config
from poem_manager import PoemManager
from audio_generator import AudioGenerator
from video_creator import VideoCreator

def main():
    print("🚀 Запуск бота для поэзии...")
    
    poem_manager = PoemManager()
    audio_gen = AudioGenerator()
    video_creator = VideoCreator()
    
    author, title, text = poem_manager.get_random_poem()
    print(f"📖 Выбрано: {title} - {author}")
    
    timestamp = int(time.time())
    audio_file = os.path.join(Config.AUDIO_DIR, f"audio_{timestamp}.mp3")
    video_file = os.path.join(Config.VIDEO_DIR, f"video_{timestamp}.mp4")
    
    try:
        print("🔊 Генерация аудио...")
        if audio_gen.text_to_speech(text, audio_file):
            print("🎬 Создание видео...")
            if video_creator.create_poetry_video(audio_file, text, author, title, video_file):
                print("✅ Видео создано успешно!")
                
                # Очистка
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                    
            else:
                print("❌ Ошибка создания видео")
        else:
            print("❌ Ошибка генерации аудио")
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()
