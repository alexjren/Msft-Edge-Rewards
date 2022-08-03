from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from random_word import RandomWords
from random import randint
import time

url = 'https://www.bing.com/'
# Chrome
driver = webdriver.Chrome('E:\Driver\chromedriver_win32\chromedriver')
driver.get(url)
time.sleep(5)

# Sign in
driver.find_element(By.CLASS_NAME, 'id_button').click()
time.sleep(randint(5,10)/5)
driver.find_element(By.NAME, 'loginfmt').send_keys('renalexj@gmail.com'+Keys.ENTER)
time.sleep(randint(10,20)/5)
driver.find_element(By.NAME, 'passwd').send_keys('Swimguy1'+Keys.ENTER)
time.sleep(randint(3,5))
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(randint(3,5))
# Generate words for the day
r=RandomWords()

for i in range(1,40):
    word=r.get_random_word()
    print(word)
    search_box=driver.find_element(By.ID,'sb_form_q')
    search_box.clear()
    search_box.send_keys(word)
    search_box.send_keys(Keys.RETURN)
    time.sleep(randint(4,6))