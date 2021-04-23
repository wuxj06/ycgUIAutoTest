__author__ = 'wuxj06'
import unittest
from PageObject.RegionSite.regionSitepage import RegionSitePage
from PageObject.Home.homepage import HomePage
from selenium import webdriver
from TestData import common_data as CD
from BeautifulReport import BeautifulReport
from Common import config


class Test_RegionSite(unittest.TestCase):
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

    @BeautifulReport.add_test_img('testARegionSiteHomePage')
    def testARegionSiteHomePage(self):
        u"""区域分站首页"""
        hp = HomePage(self.driver)
        hp.switchToRegionSite()
        rp = RegionSitePage(self.driver)
        rp.checkHomePage()

    @BeautifulReport.add_test_img('testBRecommendSupplier')
    def testBRecommendSupplier(self):
        u"""区域分站推荐供应商"""
        rp = RegionSitePage(self.driver)
        rp.checkRecommendSupplier()

    @BeautifulReport.add_test_img('testCPrice')
    def testCPrice(self):
        u"""区域分站信息价"""
        rp = RegionSitePage(self.driver)
        rp.checkPrice()

    @BeautifulReport.add_test_img('testDRecruitAndBid')
    def testDRecruitAndBid(self):
        u"""区域分站招募招标"""
        rp = RegionSitePage(self.driver)
        rp.checkRecruitAndBid()

    @BeautifulReport.add_test_img('testEItemCase')
    def testEItemCase(self):
        u"""区域分站项目案例"""
        rp = RegionSitePage(self.driver)
        rp.checkItemCase()

    @BeautifulReport.add_test_img('testFbusinessAndwinBid')
    def testFbusinessAndwinBid(self):
        u"""区域分站入库和中标"""
        rp = RegionSitePage(self.driver)
        rp.checkbusinessAndwinBid()