from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from sys import platform
import configparser
from secrets import token_hex
from bumbleAI import crop_face
import os
import shutil

# load config
config = configparser.ConfigParser()
config.read('config.INI')


def instantiate_browser():
    # Setup the chrome driver
    options = Options()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(
        options=options, executable_path=ChromeDriverManager().install())
    return driver


def sigin_bumble(driver):
    if not driver:
        return
    # Sign up via cellphone login
    driver.get("https://bumble.com/get-started")
    # Waiting 10 seconds, but might not properly work depending on how slow your interent is
    driver.implicitly_wait(10)
    try:
        # Enter in cell num and press enter
        cell_login_btn = driver.find_elements_by_class_name('button')[1]
        cell_login_btn.click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'phone').send_keys(config["bumble"]["cell"])
        home_btns = driver.find_elements_by_class_name('button')
        home_btns[1].click()

        # second page of entering pass
        driver.find_element(By.ID, "pass").send_keys(
            config["bumble"]["passcode"])
        driver.find_elements_by_class_name('button')[0].click()

        # succesful signin
        return True
    except Exception as e:
        print(e)
        return False


def get_action_buttons(driver):
    if not driver:
        return
    # get the like and dislike buttons

    action_btns = driver.find_elements(
        By.CLASS_NAME, "encounters-action__icon")
    time.sleep(2)
    dislike_button = action_btns[0]
    like_button = action_btns[2]

    return dislike_button, like_button


def download_candidate_image(driver):
    if not driver:
        return
    # Wait certain seconds before browswer laods image
    time.sleep(5)
    download_img_path = "images/download/image_" + token_hex(20) + ".png"
    imageEl = driver.find_element_by_class_name(
        "media-box__picture-image").screenshot(download_img_path)

    return download_img_path


def get_candidate(driver, is_signed_in):

    if not is_signed_in:
        return "login_err: input in the right captcha code and rerun script"

    dislike_button, like_button = get_action_buttons(driver)
    candidate_img_path = download_candidate_image(driver)
    try:
        candidate_img_cropped_path = crop_face(candidate_img_path)
        return candidate_img_cropped_path, dislike_button, like_button
    except Exception as e:
        # skip over images that can't be cropped
        dislike_button.click()
        return None, None, None


def delete_folder_images(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def quit_browser(driver):
    if not driver:
        return
    time.sleep(3)
    driver.quit()
