import pytest

from selenium import webdriver

class TestGoogle:

    def test_run_chrome(self):
        self.driver = webdriver.Chrome('./chromedriver')

        self.driver.get("https://google.com")

        self.driver.quit()