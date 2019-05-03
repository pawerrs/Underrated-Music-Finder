from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
import itertools
import song
import setup
import time

def find_comments(url, phrases, number_of_underrated_songs):

    is_opened = False
    songList = []

    # this hack ensure that Chrome will be opened only once
    if is_opened==False:
        driver = setup.setup_browser(url)

    phrases = phrases.split(';')
    while len(songList) < number_of_underrated_songs:
        
        # waiting for video to load
        time.sleep(5)

        # scrolling page down to render comments section
        driver.execute_script('window.scrollTo(0, 500);')

        # waiting for comments
        time.sleep(5)

        container=driver.find_element_by_xpath('//*[@id="contents"]')
        comments=container.find_elements_by_xpath('//*[@id="content-text"]')


        # finding songs with specific phrases in comments
        flag = False
        for comment in comments:   
            for phrase in phrases:
                if phrase in comment.text:
                    flag = True
                    break

        url = driver.current_url

        # scrolling page up to to show next video in the top right corner
        driver.execute_script('window.scrollTo(0, -500);')
        driver.find_element_by_xpath("/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='secondary']/div[@id='secondary-inner']/div[@id='related']/ytd-watch-next-secondary-results-renderer[@class='style-scope ytd-watch-flexy']/div[@id='items']/ytd-compact-autoplay-renderer[@class='style-scope ytd-watch-next-secondary-results-renderer']/div[@id='contents']/ytd-compact-video-renderer[@class='style-scope ytd-compact-autoplay-renderer']/div[@id='dismissable']/div[@class='metadata style-scope ytd-compact-video-renderer']/a[@class='yt-simple-endpoint style-scope ytd-compact-video-renderer']/h3[@class='style-scope ytd-compact-video-renderer']/span[@id='video-title']").click()

        title = driver.find_element_by_xpath("/html/body/ytd-app/div[@id='content']/ytd-page-manager[@id='page-manager']/ytd-watch-flexy[@class='style-scope ytd-page-manager hide-skeleton']/div[@id='columns']/div[@id='primary']/div[@id='primary-inner']/div[@id='info']/div[@id='info-contents']/ytd-video-primary-info-renderer[@class='style-scope ytd-watch-flexy']/div[@id='container']/h1[@class='title style-scope ytd-video-primary-info-renderer']").text

        if(flag):
            songList.append(song.Song(title, url))

    return songList