from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager 
import time

def find_comments(url, phrase):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(1920,1080)
    driver.get(url)

    time.sleep(5)

    driver.execute_script('window.scrollTo(0, 500);')

    time.sleep(5)
    # driver.execute_script('window.scrollTo(1, 2000);')
    # time.sleep(5)

    container=driver.find_element_by_xpath('//*[@id="contents"]')
    comments=container.find_elements_by_xpath('//*[@id="content-text"]')

    for comment in comments:
        if phrase in comment.text:
            flag = True
            break
        else:
            flag = False

    
    driver.execute_script('window.scrollTo(0, -500);')
    driver.find_element_by_xpath("/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='secondary']/div[@id='secondary-inner']/div[@id='related']/ytd-watch-next-secondary-results-renderer[@class='style-scope ytd-watch-flexy']/div[@id='items']/ytd-compact-autoplay-renderer[@class='style-scope ytd-watch-next-secondary-results-renderer']/div[@id='contents']/ytd-compact-video-renderer[@class='style-scope ytd-compact-autoplay-renderer']/div[@id='dismissable']/div[@class='metadata style-scope ytd-compact-video-renderer']/a[@class='yt-simple-endpoint style-scope ytd-compact-video-renderer']/h3[@class='style-scope ytd-compact-video-renderer']/span[@id='video-title']").click()


    
    # el = container.find_elements_by_xpath("//img[@id='img']")[0]
    return flag, driver.current_url
