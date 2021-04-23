__author__ = 'wuxj06'
import unittest
from PageObject.ServerDetail.serverTypeDetailPage import ServerTypeDetailPage
from PageObject.Home.homepage import HomePage
from selenium import webdriver
from TestData import common_data as CD
from BeautifulReport import BeautifulReport
from Common import config

class Test_ServerTypeDetail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def save_img(self,img_name):
        self.driver.get_screenshot_as_file('{}{}.png'.format(config.img_dir, img_name))

    @BeautifulReport.add_test_img('testAServerTypeHomePage')
    def testAServerTypeHomePage(self):
        u"""服务分类首页"""
        hp = HomePage(self.driver)
        hp.switchToServerDetail()
        sp = ServerTypeDetailPage(self.driver)
        self.assertTrue(sp.checkHomePage())

    @BeautifulReport.add_test_img('testBRecommendSupplier')
    def testBRecommendSupplier(self):
        u"""推荐供应商"""
        sp = ServerTypeDetailPage(self.driver)
        self.assertTrue(sp.checkRecommentSupplier())

    @BeautifulReport.add_test_img('testCRecruitandBid')
    def testCRecruitandBid(self):
        u"""招募招标"""
        sp = ServerTypeDetailPage(self.driver)
        self.assertTrue(sp.checkRecruitAndBid())

    @BeautifulReport.add_test_img('testDProjectCase')
    def testDProjectCase(self):
        u"""项目案例"""
        sp = ServerTypeDetailPage(self.driver)
        self.assertTrue(sp.checkProjectCase())

    @BeautifulReport.add_test_img('testEStorageandWinbid')
    def testEStorageandWinbid(self):
        u"""入库和中标"""
        sp = ServerTypeDetailPage(self.driver)
        self.assertTrue(sp.checkStorageAndWinbid())
