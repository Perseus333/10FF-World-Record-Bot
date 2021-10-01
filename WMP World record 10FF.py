from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://10fastfingers.com/typing-test/english#")

driver.find_element_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()

text_box = driver.find_element_by_id('inputfield')
text_box.click()
time.sleep(1)

while True:
    word = driver.find_elements_by_xpath('.//span[@class = "highlight"]')[0]
    text_box.send_keys(word.text)
    text_box.send_keys(Keys.SPACE)
