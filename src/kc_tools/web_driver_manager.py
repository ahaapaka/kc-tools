from typing import Optional

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from . import logger

class WebDriverManager:

    _instance = None

    _driver: Optional[WebDriver]

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(WebDriverManager, cls).__new__(cls, *args, **kwargs)
            cls._instance._driver = None
        return cls._instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit_driver()

    def get_driver(self) -> WebDriver:
        if not self._driver:
            options = webdriver.ChromeOptions()
            options.add_argument("--log-level=2")
            service = webdriver.ChromeService(service_args=["--log-path=chrome-driver.log"])
            self._driver = webdriver.Chrome(options=options, service=service)
            logger.debug("Web driver created")
        return self._driver

    def quit_driver(self):
        if self._driver:
            logger.debug("Quitting the web driver")
            self._driver.quit()
            self._driver = None
