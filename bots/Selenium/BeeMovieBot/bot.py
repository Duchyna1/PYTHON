from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.messenger.com/")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('matus.duchyna@gmail.com')
        print('password pls and pick chat')

    def start(self, xpath):
        file = open('ShrekScript.txt', 'r')
        line = file.readline()
        box = self.driver.find_element_by_xpath(xpath)
        for sentence in line.split('.'):
            print(sentence)
            box.click()
            box.send_keys(sentence)
            box.send_keys(Keys.RETURN)
        print('DONE!!!!')


bot = bot()
bot.start(input('Gimme xpath (_5rpu): '))