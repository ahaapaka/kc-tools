import time

from selenium.webdriver.chrome.webdriver import WebDriver

from . import logger
from .constants import WEBSITE_URL
from .login_page import find_login_link_and_click, wait_for_login_view, wait_until_user_has_logged_in
from .web_driver_manager import WebDriverManager


def login_to_website(driver: WebDriver) -> None:
    find_login_link_and_click(driver)
    wait_for_login_view(driver)
    print("Waiting for user to log in")
    wait_until_user_has_logged_in(driver)
    print("User has successfully logged in")
    time.sleep(20)
    logger.debug("Closing website")


def run():
    mgr = WebDriverManager()
    with mgr:
        driver = mgr.get_driver()
        driver.get(WEBSITE_URL)
        login_to_website(driver)


if __name__ == '__main__':
    run()
