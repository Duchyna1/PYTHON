from selenium import webdriver
from time import sleep

from selenium.webdriver.common.keys import Keys


class bot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://play.typeracer.com/")
        self.driver.maximize_window()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="qcCmpButtons"]/button[2]').click()
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="dUI"]/table/tbody/tr[2]/td[2]/div/div[1]/div/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td/a').click()
        sleep(4)
        while True:
            try:
                sleep(0.5)
                text = self.driver.find_element_by_xpath(
                    '//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]').get_attribute(
                    "innerHTML")
                print(text)
                self.driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').send_keys(text)
                self.driver.find_element_by_xpath('//*[@id="gwt-uid-15"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/input').send_keys(Keys.SPACE)
            except:
                print('DONE')
                break

bot()