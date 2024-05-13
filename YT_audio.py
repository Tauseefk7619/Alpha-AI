from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
class music():
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www/youtube/com/results?_query=" + query)
        video= self.driver.find_element_by_xpath('//*[@id="dismissable"}')
        video.click()



# assist=music()
# assist.play('dynamite by bts')