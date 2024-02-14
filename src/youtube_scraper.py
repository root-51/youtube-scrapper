from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import time
chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

def get_channel(url:str):
    driver.get(url)

class Tab(Enum):
    홈='홈'
    동영상='동영상'
    Shorts='Shorts'
    라이브='라이브'
    재생목록='재생목록'
    커뮤니티='커뮤니티'
    멤버십='멤버십'

def select_tab(tab_name:Tab):
    value = '[tab-title="'+tab_name.value+'"]'
    element=driver.find_element(by=webdriver.common.by.By.CSS_SELECTOR,value=value)
    if(element==None) :
        print(f'error : no element named ${tab_name}')
    return element

def click_element(element):
    try:
        element.click()
    except Exception as e:
        print('error: not clickable element')

def scroll_to_bottom():
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_all_thubnail(n:int):
    thubnails = driver.find_elements(by=webdriver.common.by.By.CSS_SELECTOR, value=".yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")
    return thubnails