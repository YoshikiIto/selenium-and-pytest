import pytest

from selenium import webdriver

class TestErrorSample:

    def setup_method(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("https://google.com")

    def teardown_method(self):
        self.driver.quit()


    def test_no_such_element(self):
        driver = self.driver
        driver.find_element_by_id("hoge").click()

    def test_sample1(self):
        driver = self.driver
        driver.quit()
        driver.find_element_by_name("q").send_keys("selenium")

