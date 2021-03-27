from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Chrome(executable_path="C:/Users/thech/Downloads/chromedriver_win32/chromedriver")
driver.get("http://twitter.com/")
sleep(3)