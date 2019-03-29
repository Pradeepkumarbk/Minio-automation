import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
import os
from slackclient import SlackClient
from selenium.common.exceptions import NoSuchElementException
# print("hi")
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driverpath = os.path.realpath("/usr/bin/chromedriver")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=driverpath)
#driver.delete_all_cookies()
driver.get("https://minio.openebs.ci")
time.sleep(1)
users = ["atul" ,"maya" ,"data" ,"kill" ,"sudo"]
#images = ["/root/Minio-automation/images/a.png"]
images = ["/home/k8s/py.mp4" ,"/home/k8s/py1.mp4","/home/k8s/py2.mp4"]
# images = ["/home/pradeep/Pictures/a.png"]
#driverpath = "/usr/bin/chromedriver"
#driver = webdriver.Chrome(driverpath)
#driver.get("https://minio.openebs.ci")
#time.sleep(2)
#n=0
#while n < 10:
   # driver = webdriver.Chrome(driverpath)
   # driver.get("https://minio.openebs.ci")
   # time.sleep(1)
   # n = n + 1
for y in users:

    time.sleep(2)
    elem = driver.find_element_by_id("accessKey")
    elem.send_keys("minio")

    elem = driver.find_element_by_xpath("//*[@id='secretKey']")
    elem.send_keys("minio123")

    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/form/button").click()
    time.sleep(2)

    driver.find_element_by_xpath("//*[@id='fe-action-toggle']/span").click()

    driver.find_element_by_xpath("//*[@id='show-make-bucket']").click()
    time.sleep(2)

    elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div/input")
    elem.send_keys(y)
    elem.send_keys(Keys.RETURN)

    driver.find_element_by_xpath("//*[@id='sidebar-toggle']").click()
    time.sleep(1)

    driver.find_element_by_xpath("//*[@id='fe-action-toggle']/span").click()
    time.sleep(1)
    for x in images:
        elem = driver.find_element_by_id("file-input")
        elem.send_keys(x)
        time.sleep(2)
    i = 0
    while i < len(images):
        try:
            time.sleep(180)
            elem = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div")
            # time.sleep(1)
            # if elem.is_displayed()://*[@id="root"]/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div[5]/div/ul/a[2]
            elem.click()
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/ul/a[2]").click()
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div[2]/button[1]").click()
            time.sleep(3)        
        i = i + 1
    # delete
    driver.find_element_by_xpath("//*[@id='sidebar-toggle']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='bucket-dropdown']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[1]/ul/li[1]/div/ul/li[2]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='top-right-menu']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='logout']").click()

driver.close()

