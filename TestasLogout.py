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

    def test_login(self):
        rastilogin = self.driver.find_element_by_id("topLoginUsername")
        rastilogin.send_keys("Zezozose")
        rastipass = self.driver.find_element_by_name("password_null")
        rastipass.clear()
        rastipass.click()
        rastipass1 = self.driver.find_element_by_name("password")

        rastipass1.send_keys("Mikroschema7089")
        rastipass1.send_keys(Keys.RETURN)
        time.sleep(5)

        rastilogout = self.driver.find_element_by_link_text("Atsijungti")
        rastilogout.click()
        assert "Registruotis" in self.driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()
