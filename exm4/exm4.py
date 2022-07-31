from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get('http://www.tsetmc.com/loader.aspx?ParTree=111C1412&inscode=62603302940123327')
driver.maximize_window()
download=driver.find_element_by_id("InsExport")
download.click()

