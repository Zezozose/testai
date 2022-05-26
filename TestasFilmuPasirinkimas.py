from lib2to3.pgen2 import driver
import unittest
from unittest import result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

class SearchTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome("E:\chromedriver.exe")
        self.driver.get("https://www.forumcinemas.lt")

    def test_search(self):
        rasti = self.driver.find_element_by_id("Movies_input")
        rasti.click()
        rastifilma = self.driver.find_element_by_id("Movies_input_308578")
        rastifilma.click()
        time.sleep(5)
        assert "Raudonoji panda" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
