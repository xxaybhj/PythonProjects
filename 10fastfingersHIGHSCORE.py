# 10fastfingers.com bot to get the best score

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys, os

os.system('cls')

browser = webdriver.Firefox()
browser.get("https://10fastfingers.com/typing-test/english")
buttonDeny = browser.find_element(By.ID, "CybotCookiebotDialogBodyButtonDecline")
buttonDeny.click()
elem = browser.find_element(By.ID, "inputfield")
elem.clear()
while True:
    try:
        word = browser.find_element(By.CLASS_NAME, "highlight").text
    except:
        print("Done")
        sys.exit()
    elem.send_keys(word+" ")
