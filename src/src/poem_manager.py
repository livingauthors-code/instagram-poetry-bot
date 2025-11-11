import pandas as pd
import random
import os
from config import Config

class PoemManager:
    def __init__(self):
        self.poems_df = self._load_poems()
        self.posted_poems = self._load_posted_poems()
    
    def _load_poems(self):
        if not os.path.exists(Config.POEMS_CSV):
            sample_data = {
                'author': ['А.С. Пушкин', 'М.Ю. Лермонтов', 'С.А. Есенин'],
                'title': ['Я помню чудное мгновенье', 'Парус', 'Береза'],
                'text': [
                    'Я помню чудное мгновенье:\nПередо мной явилась ты,\nКак мимолетное виденье,\nКак гений чистой красоты.',
                    'Белеет парус одинокой\nВ тумане моря голубом!..\nЧто ищет он в стране далекой?\nЧто кинул он в краю родном?..',
                    'Белая береза\nПод моим окном\nПринакрылась снегом,\nТочно серебром.'
                ]
            }
            df = pd.DataFrame(sample_data)
            df.to_csv(Config.POEMS_CSV, index=False, encoding='utf-8')
            return df
        return pd.read_csv(Config.POEMS_CSV, encoding='utf-8')
    
    def _load_posted_poems(self):
        if os.path.exists(Config.POSTED_POEMS_FILE):
            with open(Config.POSTED_POEMS_FILE, 'r', encoding='utf-8') as f:
                return set(line.strip() for line in f)
        return set()
    
    def get_random_poem(self):
        available_poems = self.poems_df[~self.poems_df['title'].isin(self.posted_poems)]
        
        if available_poems.empty:
            self.posted_poems.clear()
            available_poems = self.poems_df
        
        poem = available_poems.sample(n=1).iloc[0]
        return poem['author'], poem['title'], poem['text']
    
    def mark_as_posted(self, title):
        self.posted_poems.add(title)
        with open(Config.POSTED_POEMS_FILE, 'a', encoding='utf-8') as f:
            f.write(title + '\n')
    
    def get_available_backgrounds(self):
        backgrounds = []
        for file in os.listdir(Config.BACKGROUNDS_DIR):
            if file.lower().endswith(('.mp4', '.mov', '.avi')):
                backgrounds.append(os.path.join(Config.BACKGROUNDS_DIR, file))
        return backgrounds
