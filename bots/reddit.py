from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

mail = "matus.duchyna@gmail.com"

class bot:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
        self.driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe", options=chrome_options)
        self.driver.get('https://www.reddit.com/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div[1]/div/div[2]/div[2]/div[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div/nav/ul/li[3]/button').click()
        self.driver.find_element_by_xpath('//*[@id="container"]/div/nav/ul/a').click()
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
        self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[1]/div[1]/div/div/div[2]/div/div[3]/form/div[5]/button').click()
