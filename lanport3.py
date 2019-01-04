#lanport version 3
from selenium import webdriver

protocol = 'https://'
print ("Please enter the IP address")
IP = input()
address = protocol + IP + ":4343"

chromeDriverPath = "C:/Users//Downloads/chromedriver_win32/chromedriver.exe"
browser = webdriver.Chrome(chromeDriverPath)
browser.get(address)

username = browser.find_element_by_id('username_input')
domain   = browser.find_element_by_id('domain_input')

username.send_keys('')
domain.send_keys('')
