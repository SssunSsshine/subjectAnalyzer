from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


class ChromeDriverManager:
    def __init__(self):
        self.driver_path = 'D:/User/unic/chromedriver-win64/chromedriver.exe'
        self.driver = None

    def start(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Запуск браузера в фоновом режиме

        service = ChromeService(self.driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def stop(self):
        if self.driver:
            self.driver.quit()
            self.driver = None