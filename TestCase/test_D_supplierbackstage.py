#encoding=utf-8
__author__ = 'wuxj06'
import pytest
import allure
from PageObject.BackStage.supplierBackStage import SupplierBackStage

@pytest.mark.usefixtures('init_supplier_login')
class Test_SupplierBackStage():

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'供应商工作台')
    def testASupplierWorkStation(self,init_supplier_login):
        u"""供应商后台——供应商工作台"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkWorkStation()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'个人设置')
    def testAUserSetting(self,init_supplier_login):
        u"""供应商后台——个人设置"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkUserSetting()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'营销数据统计')
    def testBDataCount(self,init_supplier_login):
        u"""供应商后台——营销数据统计"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkDatacount()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'市场数据分析')
    def testCDataAnalysis(self,init_supplier_login):
        u"""供应商后台——市场数据分析"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkDataAnalysis()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'通知')
    def testDNotice(self,init_supplier_login):
        u"""供应商后台——通知"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkMessage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'待报名')
    def testESignUp(self,init_supplier_login):
        u"""供应商后台——待报名"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkSignUp()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'我的招标')
    def testFMyBidding(self,init_supplier_login):
        u"""供应商后台——我的招标"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkMybidding()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'我的招募')
    def testGMyrecruit(self,init_supplier_login):
        u"""供应商后台——我的招募"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkMyrecruit()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'主动申请入库')
    def testHRecruitApply(self,init_supplier_login):
        u"""供应商后台——主动申请入库"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkRecruitApply()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'采招门户管理')
    def testIMenhuManage(self,init_supplier_login):
        u"""供应商后台——采招门户管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkMenhumanage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'资格预审表')
    def testJRegisterIndex(self,init_supplier_login):
        u"""供应商后台——资格预审表"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkRegistrationindex()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'名片交换')
    def testKBuscard(self,init_supplier_login):
        u"""供应商后台——名片交换"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkBuscard()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'入库管理')
    def testLStorage(self,init_supplier_login):
        u"""供应商后台——入库管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkStorage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'我的对接会')
    def testMOnlineMeeting(self,init_supplier_login):
        u"""供应商后台——我的对接会"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkOnlinemeeting()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'企业档案')
    def testNSupplierArchive(self,init_supplier_login):
        u"""供应商后台——企业档案"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkSupplierArchive()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'中标发布')
    def testOWinbidPublic(self,init_supplier_login):
        u"""供应商后台——中标发布"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkWinbid()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'案例管理')
    def testPCaseManage(self,init_supplier_login):
        u"""供应商后台——案例管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkCaseManage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'产品管理')
    def testQProductManagge(self,init_supplier_login):
        u"""供应商后台——产品管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkProductManage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'企业风采')
    def testRAritcleList(self,init_supplier_login):
        u"""供应商后台——企业风采"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkArticleList()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'展厅轮播图')
    def testShowRoom(self,init_supplier_login):
        u"""供应商后台——展厅轮播图"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkShowroom()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'广告位管理')
    def testTAdmanage(self,init_supplier_login):
        u"""供应商后台——广告位管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkAdmanage()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'定向推广')
    def testUTargetedPromotion(self,init_supplier_login):
        u"""供应商后台——定向推广"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkTargetedPromotion()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'二级域名')
    def testVDomain(self,init_supplier_login):
        u"""供应商后台——二级域名"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkDomain()

    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'账号管理')
    def testWAccountManage(self,init_supplier_login):
        u"""供应商后台——账号管理"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkAccountManage()

    @pytest.mark.flaky(reruns=1)
    @pytest.mark.smoke
    @allure.feature(u'供应商后台')
    @allure.story(u'企业展厅')
    def testXCompanyHall(self,init_supplier_login):
        u"""供应商后台——企业展厅"""
        sb = SupplierBackStage(init_supplier_login)
        assert sb.checkCompanyHall()


