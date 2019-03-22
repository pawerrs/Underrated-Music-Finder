from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
import time

def find_comments(url, phrase):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    driver.execute_script('window.scrollTo(1, 500);')

    time.sleep(2)

    #driver.execute_script('window.scrollTo(1, 3000);')

    container=driver.find_element_by_xpath('//*[@id="contents"]')
    comments=container.find_elements_by_xpath('//*[@id="content-text"]')

    for comment in comments:
        if phrase in comment:
            flag = True
            break
        else:
            flag = False
    
    return flag
