from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def init_setup():
    driver_path = Service(r"/usr/local/bin/chromedriver.exe")
    op = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service = driver_path, options = op)
    return driver