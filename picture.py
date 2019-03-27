import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import os
print("hi")
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("--test-type")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driverpath = os.path.realpath("/usr/bin/chromedriver")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driverpath)
driver.get("https://minio-dashboard.openebs100.io")
#driver.get("https://minio.openebs.ci")
driver.save_screenshot("screenshot2.png")
time.sleep(5)
print("hi")
elem = driver.find_element_by_id("accessKey")
elem.send_keys("minio")
print("hi")
elem = driver.find_element_by_xpath("//*[@id='secretKey']")
elem.send_keys("minio123")
print("hi")

