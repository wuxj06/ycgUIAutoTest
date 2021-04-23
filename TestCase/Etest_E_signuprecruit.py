__author__ = 'wuxj06'
import unittest
from PageObject.Home.recruitpage import RecruitPage
from PageObject.Login.loginPage import LoginPage
from selenium import webdriver
from TestData import common_data as CD
from BeautifulReport import BeautifulReport
from Common import config

class Test_SignUpRecruit(unittest.TestCase):
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

    @BeautifulReport.add_test_img('testSignUpRecruit')
    def testSignUpRecruit(self):
        u"""供应商报名招募"""
        rp = RecruitPage(self.driver)
        self.assertTrue(rp.signUpRecruit())

