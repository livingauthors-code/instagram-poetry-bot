import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from config import Config

class InstagramPoster:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None
    
    def setup_driver(self):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
    
    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            time.sleep(3)
            
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys(self.username)
            
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(self.password)
            password_input.send_keys(Keys.RETURN)
            
            time.sleep(5)
            return True
            
        except Exception as e:
            print(f"Ошибка при логине: {e}")
            return False
    
    def close(self):
        if self.driver:
            self.driver.quit()
