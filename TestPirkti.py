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
        rasti = self.driver.find_element_by_id("naviLink3")
        rasti.click()
        rasti = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[6]/div[1]/div/div/div[3]/a[3]")
        rasti.click()
        rasti = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[12]/div[1]/div/div/div/div[1]/div[2]/div[1]/div/table/tbody/tr[1]/td[3]/strong/a")
        rasti.click()
        rasti = self.driver.find_element_by_id("product13361Amount_input")
        rasti.click()
        rasti = self.driver.find_element_by_id("product13361Amount_input_2")
        rasti.click()
        rasti = self.driver.find_element_by_class_name("buttonLight")
        rasti.click()
        time.sleep(5)
        assert "Prisijungti" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
