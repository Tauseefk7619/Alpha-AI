from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'


class infow:
    def __init__(self):
        self.query = None
        service = Service(chromedriver_path)
        self.driver = webdriver.Chrome(service=service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button/i')
        enter.click()