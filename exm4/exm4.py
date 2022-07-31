from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import glob
import os
listurl=['http://www.tsetmc.com/loader.aspx?ParTree=111C1412&inscode=22667016906590506']
chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : "/home/mamadtnt/Desktop/excel"}
chromeOptions.add_experimental_option("prefs",prefs)
chromedriver = "/usr/bin/chromedriver"
driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
# driver = webdriver.Chrome('/usr/bin/chromedriver')
for url in listurl:
    driver.get(url)
    driver.maximize_window()
    btn_1=WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.ID, "InsExport")))
    btn_1.click()
    time.sleep(5)
    list_of_files = glob.glob('/home/mamadtnt/Desktop/excel/*.csv', recursive=True)
    latest_file = max(list_of_files, key=os.path.getctime)
    os.rename(latest_file, '/home/mamadtnt/Desktop/excel/'+driver.title.split(' ')[0]+'.csv')