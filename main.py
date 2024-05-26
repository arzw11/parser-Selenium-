from selenium import webdriver
from selenium.webdriver.common.by import By
import json


class ParserLis:
    def __init__(self):
        self.url = "https://lis-skins.ru/market/csgo/container/"
        self.titles = []
        self.prices = []
        self.discount = []
        self.links = []

    def get_info(self):
        with webdriver.Chrome() as browser:
            info_dict = []
            browser.get(self.url)
            finder = browser.find_element(By.CLASS_NAME, "skins-market-skins-list ")
            self.titles = [x.text for x in browser.find_elements(By.CLASS_NAME, "name")]
            self.prices = [
                x.text.split(".cls")[0]
                for x in browser.find_elements(By.CLASS_NAME, "price")
            ]
            self.discount = [
                x.text
                for x in browser.find_elements(By.CLASS_NAME, "steam-price-discount")
            ]
            self.links = [
                x.get_attribute("href") for x in finder.find_elements(By.TAG_NAME, "a")
            ]
        for x in list(zip(self.titles, self.prices, self.discount, self.links)):
            info_dict.append(
                {
                    "Название": x[0],
                    "Цена": x[1],
                    "Скидка": x[2],
                    "Ссылка": x[3],
                }
            )
        print("Информация изъята")
        return info_dict

    def write_info(self):
        with open("result.json", "w", encoding="utf-8") as file:
            json.dump(self.get_info(), file, indent=4, ensure_ascii=False)
        print("Информация записана")


parser = ParserLis()
reusult = parser.write_info()
