from selenium import webdriver
from time import sleep
import sys

sys.setrecursionlimit(1000000)

class bot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://mouseaccuracy.com")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/div/div[1]/ul[1]/li[2]/div[2]/a[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/div/div[1]/ul[1]/li[2]/div[2]/a[2]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/div/div[1]/ul[2]/li[2]/div[2]/a[1]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/div/div[1]/ul[3]/li[2]/div[2]/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/a').click()
        sleep(4)
        print('start')
        x = []
        self.start(x)

    def start(self, prev):
        now = self.driver.find_elements_by_class_name('target')
        if now:
            targets = self.Diff(now, prev)
            print(targets)
            for target in targets:
                target.click()
            self.start(now)
        else:
            print('done')

    def Diff(self, li1, li2):
        return (list(set(li1) - set(li2)))