#encoding=utf-8
__author__ = 'wuxj06'
from PageObject.BackStage.devBackStage import DevBackStage
import pytest
import allure

@pytest.mark.usefixtures('init_dev_login')
class Test_DevBackStage():
    
    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'开发商后台首页')
    def testAStation(self,init_dev_login):
        """开发商工作台"""
        db = DevBackStage(init_dev_login)
        assert db.checkStation()

    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'招募管理')
    def testBRecruitManage(self,init_dev_login):
        """招募管理"""
        db = DevBackStage(init_dev_login)
        assert db.checkRecruitManage()
    
    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'供应商管理')
    def testCSupplierManage(self,init_dev_login):
        """供应商管理"""
        db = DevBackStage(init_dev_login)
        assert db.checkSupplierManage()

    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'招标管理')
    def testDBiddingManage(self,init_dev_login):
        """招标管理"""
        db = DevBackStage(init_dev_login)
        assert db.checkBiddingManage()

    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'基础设置')
    def testEBasicSetting(self,init_dev_login):
        """基础设置"""
        db = DevBackStage(init_dev_login)
        assert db.checkBasicSetting()

    @pytest.mark.smoke
    @allure.feature(u'开发商后台')
    @allure.story(u'供应商评估')
    def testFSupplierInspect(self,init_dev_login):
        """供应商评估"""
        db = DevBackStage(init_dev_login)
        assert db.checkInspect()

