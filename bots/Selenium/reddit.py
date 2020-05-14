from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import random

from selenium.webdriver.common.keys import Keys


class bot:

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        sleep(1)
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=chrome_options)
        sleep(1)
        self.driver.get('https://www.reddit.com/')
        sleep(1)
        self.driver.maximize_window()
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div/nav/ul/li[5]/button').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/nav/ul/li[1]/a').click()
        self.upvotes = []
        print('please log in')
        print('\"bot.toMemes()\" to continue')

    def toMemes(self):
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div/nav/ul/li[4]/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/nav/ul/div/div[2]/form/input[2]').send_keys('memes')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="container"]/div/nav/ul/div/div[2]/form/input[2]').send_keys(Keys.RETURN)
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div/div/div/div/nav/div[1]/div[1]/div/div[1]/span[2]').click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div/div/div/div/nav/div[1]/div[1]/div/div[2]/div/div[3]/div[4]/div[2]').click()
        sleep(1)
        self.start()

    def start(self):
        self.upvotes = self.driver.find_elements_by_class_name('icon-upvote')
        sleep(2)
        for upvote in self.upvotes:
            sleep(random())
            upvote.click()
        print("page done")
        self.driver.refresh()
        sleep(2)
        self.start()

print("\"bot = bot()\" to start")