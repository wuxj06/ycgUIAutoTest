__author__ = 'wuxj06'
import unittest
from PageObject.Home.biddingpage import BiddingPage
from PageObject.Login.loginPage import LoginPage
from selenium import webdriver
from TestData import common_data as CD
from BeautifulReport import BeautifulReport
from Common import config

class Test_SignUpbid(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        lp = LoginPage(cls.driver)
        lp.login(CD.url,CD.username_supplier,CD.password_supplier)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}{}.png'.format(config.img_dir, img_name))

    @BeautifulReport.add_test_img('testSignupBid')
    def testSignupBid(self):
        u"""供应商报名招标"""
        rp = BiddingPage(self.driver)
        self.assertTrue(rp.signUpbid())

