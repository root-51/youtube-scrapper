from enum import Enum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

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
    element=driver.find_element(by=webdriver.common.by.By.CSS_SELECTOR,value='[tab-title="홈"]')
    if(element==None) :
        print(f'error : no element named ${tab_name}')
    return element