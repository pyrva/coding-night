from get_gecko_driver import GetGeckoDriver
from selenium import webdriver

gecko = GetGeckoDriver()
gecko.install()

driver = webdriver.Firefox()
