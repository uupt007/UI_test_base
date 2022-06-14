import os
from time import sleep
from selenium import webdriver
from config.read_ini import ReadIni
from selenium.webdriver.chrome.service import Service

#  工程路径
parent_path = os.path.dirname(os.path.dirname(__file__))
#  读取配置文件对象
sqxy= ReadIni()
#  获取被测网站
url = sqxy.get_value("url")
def get_chrome_driver():
    driver_path = Service(parent_path +"./driver/chromedriver.exe")
    driver = webdriver.Chrome(service=driver_path)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(3)
    return driver
if __name__ == '__main__':
    get_chrome_driver()
