from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from sys import platform
import configparser

config = configparser.ConfigParser()
config.read('config.INI')

# Setup the chrome driver
options = Options()
options.page_load_strategy = 'eager'

driver = webdriver.Chrome(
    options=options, executable_path=ChromeDriverManager().install())

# Sign up via cellphone login
driver.get("https://bumble.com/get-started")
# Waiting 10 seconds, but might not properly work depending on how slow your interent is
driver.implicitly_wait(10)

# Enter in cell num and press enter
cell_login_btn = driver.find_elements_by_class_name('button')[1]
cell_login_btn.click()
driver.implicitly_wait(5)
driver.find_element(By.ID, 'phone').send_keys(config["bumble"]["cell"])
home_btns = driver.find_elements_by_class_name('button')
home_btns[1].click()

# second page of entering pass
driver.find_element(By.ID, "pass").send_keys(config["bumble"]["passcode"])
driver.find_elements_by_class_name('button')[0].click()
# driver.quit()

driver.implicitly_wait(5)
action_btns = driver.find_elements(By.CLASS_NAME, "encounters-action__icon")
driver.implicitly_wait(5)
dislike_button = action_btns[0]
like_button = action_btns[2]

# like people based on the AI
# like_button.click()
