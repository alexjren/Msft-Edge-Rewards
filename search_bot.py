from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random_word import RandomWords
from random import randint
import time
import datetime

url = 'https://www.bing.com/'
# Chrome
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome('E:\Driver\chromedriver_win32\chromedriver', chrome_options=options)
#driver = webdriver.Chrome('E:\Driver\chromedriver_win32\chromedriver')
driver.get(url)
time.sleep(5)

# Sign in
driver.find_element(By.CLASS_NAME, 'id_button').click()
time.sleep(randint(5,10)/5)
driver.find_element(By.NAME, 'loginfmt').send_keys('renalexj@gmail.com'+Keys.ENTER)
time.sleep(randint(10,20)/5)
driver.find_element(By.NAME, 'passwd').send_keys('Swimguy1'+Keys.ENTER)
time.sleep(randint(2,4))
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(randint(2,4))
# Generate words for the day
r=RandomWords()


while True:
    date=datetime.date(1,1,1)
    datetime1=datetime.datetime.combine(date,datetime.time(16,0,0))
    datetime2=datetime.datetime.combine(date,datetime.datetime.now().time())
    sleeptime=datetime1-datetime2
    stoptime=sleeptime.total_seconds()
    if stoptime<0:
        stoptime=(sleeptime+datetime.timedelta(days=1)).total_seconds()
    time.sleep(stoptime)
    for i in range(1,40):
        word=r.get_random_word()
        while word is None:
            word=r.get_random_word()
        print(str(i)+" "+word)
        search_box=driver.find_element(By.ID,'sb_form_q')
        search_box.clear()
        search_box.send_keys(word)
        search_box.send_keys(Keys.RETURN)
        time.sleep(randint(1,3))
