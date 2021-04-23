#encoding=utf-8
__author__ = 'wuxj06'

from PageObject.Home.homepage import HomePage
import pytest
import allure

@pytest.mark.usefixtures('init_supplier_login')
class Test_Home():
    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'首页')
    def testAHome(self,init_supplier_login):
        """首页"""
        hp = HomePage(init_supplier_login)
        hp.checkHomePage()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'寻源页面')
    def testBSearch(self,init_supplier_login):
        """寻源"""
        hp = HomePage(init_supplier_login)
        hp.checkSearch()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'招募招标页面')
    def testCRecruitAndBidding(self,init_supplier_login):
        """招募招标"""
        hp = HomePage(init_supplier_login)
        hp.checkRecruitAndBidding()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'入驻企业页面')
    def testDSettledCompany(self,init_supplier_login):
        """入驻企业"""
        hp = HomePage(init_supplier_login)
        hp.checkSettledCompany()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'采招平台页面')
    def testECaizhao(self,init_supplier_login):
        """采招平台"""
        hp = HomePage(init_supplier_login)
        hp.checkCaizhaoStation()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'企业社区页面')
    def testFZone(self,init_supplier_login):
        """行业社区"""
        hp = HomePage(init_supplier_login)
        hp.checkZone()

    @pytest.mark.smoke
    @allure.feature(u'首页')
    @allure.story(u'资讯页面')
    def testGZixun(self,init_supplier_login):
        """资讯"""
        hp = HomePage(init_supplier_login)
        hp.checkZixun()
