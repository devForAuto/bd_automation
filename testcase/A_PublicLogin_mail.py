# -*- coding: utf-8 -*-
"""

@file: A_PublicLogin.py

@time: 2017/9/20 10:28

@desc:

"""
from base.base_driver import browser
import unittest

class PublicLogin(unittest.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_public_login(self):
        url = "http://www.baidu.com"
        self.driver.get(url)
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()