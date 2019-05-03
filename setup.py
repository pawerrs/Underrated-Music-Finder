from selenium import webdriver
from selenium.webdriver.chrome.options import Options  

def setup_browser(url):
    path_To_Extension = r'C:\Users\pawer\Desktop\3.44.0_0'
    chrome_options = Options()

    #loading Adblock to disable ads
    chrome_options.add_argument('load-extension=' + path_To_Extension)
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # setting full size of browser. Only this mode allows to render comments 
    driver.set_window_size(1920,1080)

    driver.create_options()

    #opening YouTube video
    driver.get(url)
    
    # autoswitching to YouTube tab 
    window_name = driver.window_handles[0]
    driver.switch_to.window(window_name=window_name)

    return driver