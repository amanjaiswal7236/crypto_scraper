# scraper/coinmarketcap.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class CoinMarketCap:
    def __init__(self):
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        

    def scrape_coin_data(self, coin):
        url = f'https://coinmarketcap.com/currencies/{coin}/'
        self.driver.get(url)
        time.sleep(5)

        # Extract data
        data = {
            "price": self.get_element_text(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/section/div/div[2]/span"),
            "market_cap": self.get_element_text(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/section[2]/div/div[1]/div/dl/div[1]/div[1]/dd"),
            # Add other fields similarly
        }

        return data

    def get_element_text(self, by, value):
        try:
            return self.driver.find_element(by, value).text
        except:
            return None

    def close(self):
        self.driver.quit()
