from typing import Final

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import logger
from .constants import PAGE_LOAD_WAIT_TIMEOUT

USER_LOGIN_WAIT_TIMEOUT: Final[float] = 60.0
LOGIN_PAGE_TITLE_DEFAULT: Final[str] = "Sign in"
USERNAME_PROMPT_DEFAULT: Final[str] = "Email"
PASSWORD_PROMPT_DEFAULT: Final[str] = "Password"


def find_login_link_and_click(driver: WebDriver):
    login_link = driver.find_element(By.ID, "login-link")
    driver.execute_script("arguments[0].scrollIntoView();", login_link)
    actions = ActionChains(driver)
    actions.move_to_element(login_link).perform()
    login_link.click()


def wait_for_login_view(driver: WebDriver):
    try:
        WebDriverWait(driver, PAGE_LOAD_WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, "loginview")))
    except TimeoutException as e:
        raise TimeoutException(f"Login view did not appear in {PAGE_LOAD_WAIT_TIMEOUT} s") from e


def get_login_page_title(driver: WebDriver) -> str:
    try:
        title_element = driver.find_element(By.CLASS_NAME, "loginview__title")
        return title_element.text
    except NoSuchElementException:
        logger.warn("Could not find login header element")
    return LOGIN_PAGE_TITLE_DEFAULT

def get_email_prompt(driver: WebDriver) -> str:
    try:
        login_view_div = driver.find_element(By.ID, "loginview")
        label_texts = login_view_div.find_elements(By.CLASS_NAME, "d4-label__text")
        if len(label_texts) == 2:
            return label_texts[0].text
    except NoSuchElementException:
        logger.warn("Could not find username prompt element")
    return USERNAME_PROMPT_DEFAULT


def get_password_prompt(driver: WebDriver) -> str:
    try:
        login_view_div = driver.find_element(By.ID, "loginview")
        label_texts = login_view_div.find_elements(By.CLASS_NAME, "d4-label__text")
        if len(label_texts) == 2:
            return label_texts[1].text
    except NoSuchElementException:
        logger.warn("Could not find password prompt element")
    return PASSWORD_PROMPT_DEFAULT


def wait_until_user_has_logged_in(driver: WebDriver):
    try:
        WebDriverWait(driver, USER_LOGIN_WAIT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//*[@id='userbar']/nav")))
    except TimeoutException as e:
        raise TimeoutException(f"Login not detected after waiting for {USER_LOGIN_WAIT_TIMEOUT} s") from e
