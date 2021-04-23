__author__ = 'wuxj06'
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from Common import Logger,config
import time
from selenium.webdriver.common.keys import Keys
from PageObject.Home.homepage import HomePage

class DevBackStage(BasePage):


    def checkStation(self):
        hp = HomePage(self.driver)
        hp.switchToBackStage()
        logging.info("——检查开发商工作台界面——")
        #判断是否有弹框，有的话就关闭
        if self.is_element_exist(By.XPATH,self.station["closebtn"]):
            self.find_element(By.XPATH,self.station["closebtn"]).click()
        elif self.is_element_exist(By.XPATH,self.station["dialogclose1"]):
            self.find_element(By.XPATH,self.station["dialogclose1"]).click()
        elif self.is_element_exist(By.XPATH,self.station["dialogclose2"]):
            self.find_element(By.XPATH,self.station["dialogclose2"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.station["publishrecruit"])):
                logging.info("——开发商工作台界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——工作台界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecruitManage(self):
        logging.info("——检查招募管理界面——")
        try:
            self.find_element(By.XPATH,self.recruitManage["menu"]).click()
            self.switchToRecruitList()
            self.switchToCard()
            self.switchToUnsuitableSupplier()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToRecruitList(self):
        logging.info("——检查招募列表——")
        try:
            if(self.is_element_exist(By.XPATH,self.recruitManage["publishrecruit"])):
                logging.info("——招募列表显示正常——")
                time.sleep(2)
                status=self.publushRecruit()
                return status
            else:
                logging.info("——招募列表显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg
    #发布招募
    def publushRecruit(self):
        logging.info("——发布招募——")
        self.find_element(By.XPATH,self.recruitManage["publishrecruit"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.publishrecruit["typeList"])):
                self.find_element(By.XPATH,self.publishrecruit["typeList"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["level1"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["level2"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["level3"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["ok1"]).click()
                name1 = self.find_element(By.XPATH,self.publishrecruit["recruitname"]).get_attribute('value')
                self.find_element(By.XPATH,self.publishrecruit["registerEndDate"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["registerEndTime"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["ok2"]).click()
                time.sleep(1)
                iframe = self.find_element(By.XPATH,self.publishrecruit["iframe"])
                self.driver.switch_to.frame(iframe)
                self.find_element(By.XPATH,self.publishrecruit["content"]).send_keys("this is test message,just ingore it")
                self.driver.switch_to.default_content()
                self.execute_js("var q=document.documentElement.scrollTop=10000")
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["severArea"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["china"]).click()
                self.find_element(By.XPATH,self.publishrecruit["registerFound"]).send_keys('10')
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["ownlist"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["own"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["prepublish"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["publish"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishrecruit["view"]).click()
                time.sleep(1)
                name2=self.find_element(By.XPATH,self.publishrecruit["recruit"]).text
                assert name1==name2
                logging.info("——发布招募成功——")
                return True
            else:
                logging.info("——发布招募失败——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg


    def switchToCard(self):
        logging.info("——检查名片交换——")
        self.find_element(By.XPATH,self.recruitManage["buscard"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.recruitManage["mycard"])):
                logging.info("——名片交换界面显示正常——")
                self.find_element(By.XPATH,self.recruitManage["mycard"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.recruitManage["cancel"]).click()
                time.sleep(2)
                return True
            else:
                logging.info("——名片交换显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToUnsuitableSupplier(self):
        logging.info("——检查不合适供应商界面——")
        self.find_element(By.XPATH,self.recruitManage["unsuitable"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.recruitManage["search"])):
                logging.info("——不合适的供应商界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——不合适的供应商界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkSupplierManage(self):
        logging.info("——检查供应商管理界面——")
        try:
            self.find_element(By.XPATH,self.supplierManage["menu"]).click()
            assert self.switchToApllyIn()
            assert self.switchToSupplierStore()
            assert self.switchToSupplierCollect()
            assert self.switchToRecycle()
            assert self.switchToRegistrationlist()
            assert self.switchToTemplate()
            assert self.switchToAttachTempalte()
            assert self.switchToMymeeting()
            assert self.switchToImportSupplier()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            raise msg

    def switchToApllyIn(self):
        logging.info("——检查主动申请入库界面——")
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["supplier"])):
                logging.info("——主动申请入库界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——主动申请入库界面显示有问题")
                time.sleep(2)
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            raise msg

    def switchToSupplierStore(self):
        logging.info("——检查供方储备库界面——")
        self.find_element(By.XPATH,self.supplierManage["storagesupplier"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["listcontent"])):
                logging.info("——供方储备库界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——供方储备库界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToSupplierCollect(self):
        logging.info("——检查供应商收藏界面——")
        self.find_element(By.XPATH,self.supplierManage["favorite"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["suppliername"])):
                logging.info("——供应商收藏界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——供应商收藏界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToRecycle(self):
        logging.info("——检查回收站界面——")
        self.find_element(By.XPATH,self.supplierManage["recycle"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["search"])):
                logging.info("——回收站界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——回收站界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToRegistrationlist(self):
        logging.info("——检查收发登记表界面——")
        self.find_element(By.XPATH,self.supplierManage["registrationlist"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["inviteBtn"])):
                logging.info("——收发登记表界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——收发登记表界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToTemplate(self):
        logging.info("——检查登记表模板界面——")
        self.find_element(By.XPATH,self.supplierManage["template"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["createModule1"])):
                logging.info("——登记表模板界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——登记表模板界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToAttachTempalte(self):
        logging.info("——检查附件模板界面——")
        self.find_element(By.XPATH,self.supplierManage["attachtempalte"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["createModule2"])):
                logging.info("——附件模板界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——附件模板界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToImportSupplier(self):
        logging.info("——检查旧版导入供应商界面——")
        self.find_element(By.XPATH,self.supplierManage["importSupplier"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["importBtn"])):
                logging.info("——旧版导入供应商界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——旧版导入供应商界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToMymeeting(self):
        logging.info("——检查我的对接会界面——")
        self.find_element(By.XPATH,self.supplierManage["mymeeting"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierManage["th"])):
                logging.info("——我的对接会界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——我的对接会界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkBiddingManage(self):
        logging.info("——检查招标管理界面——")
        self.find_element(By.XPATH,self.bidManage["menu"]).click()
        try:
            assert self.switchToBidList()
            assert self.switchToDraft()
            assert self.switchToArchive()
            assert self.switchToWinBid()
            assert self.switchToPublishBid()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg


    def switchToBidList(self):
        logging.info("——检查招标列表界面——")
        try:
            if(self.is_element_exist(By.XPATH,self.bidManage["filter"])):
                logging.info("——招标列表界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——招标列表商界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToDraft(self):
        logging.info("——检查草稿箱界面——")
        self.find_element(By.XPATH,self.bidManage["draft"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.bidManage["publishBid"]) or self.is_element_exist(By.XPATH,self.bidManage["operate"])):
                logging.info("——草稿箱界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——草稿箱界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToArchive(self):
        logging.info("——检查招标公告归档——")
        self.find_element(By.XPATH,self.bidManage["archive"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.bidManage["exportBtn"])):
                logging.info("——招标公告归档显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——招标公告归档显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToWinBid(self):
        logging.info("——检查中标公告界面——")
        self.find_element(By.XPATH,self.bidManage["winbidBtn"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.winbid["createWinbid"])):
                logging.info("——发布中标公告——")
                self.find_element(By.XPATH,self.winbid["createWinbid"]).click()
                time.sleep(1)
                name1 = u'中标公告测试%s'%time.strftime("%Y%m%d.%H.%M.%S")
                self.find_element(By.XPATH,self.winbid["name"]).send_keys(name1)
                self.find_element(By.XPATH,self.winbid["serverType"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.winbid["level1"]).click()
                self.find_element(By.XPATH,self.winbid["level2"]).click()
                self.find_element(By.XPATH,self.winbid["level3"]).click()
                self.find_element(By.XPATH,self.winbid["ok1"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.winbid["winbidsupplier"]).click()
                self.find_element(By.XPATH,self.winbid["add"]).click()
                self.find_element(By.XPATH,self.winbid["ok2"]).click()
                self.find_element(By.XPATH,self.winbid["detail"]).send_keys("good good study,day day up")
                self.find_element(By.XPATH,self.winbid["submit"]).click()
                time.sleep(3)
                name2 = self.find_element(By.XPATH,self.winbid["winbidname"]).text
                assert name1 == name2
                logging.info("——创建中标公告成功——")
                return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToPublishBid(self):
        logging.info("——检查发布招标界面——")
        self.find_element(By.XPATH,self.bidManage["publishBidMenu"]).click()
        time.sleep(1)
        logging.info("——发布招标——")
        try:
            if(self.is_element_exist(By.XPATH,self.publishbid["bidname"])):
                bidname = u"招标测试%s"%(str(int(time.time())))
                self.find_element(By.XPATH,self.publishbid["bidname"]).send_keys(bidname)
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["companyList"]).click()
                self.find_element(By.XPATH,self.publishbid["company"]).click()
                self.find_element(By.XPATH,self.publishbid["bidTypeList"]).click()
                self.find_element(By.XPATH,self.publishbid["level1"]).click()
                self.find_element(By.XPATH,self.publishbid["level2"]).click()
                self.find_element(By.XPATH,self.publishbid["level3"]).click()
                self.find_element(By.XPATH,self.publishbid["ok1"]).click()
                self.find_element(By.XPATH,self.publishbid["projectlist"]).click()
                self.find_element(By.XPATH,self.publishbid["project"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["ok2"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["registerEndDate"]).click()
                time.sleep(1)
                iframe = self.find_element(By.XPATH,self.publishbid["frame"])
                self.driver.switch_to.frame(iframe)
                self.find_element(By.XPATH,self.publishbid["registerDate"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["ok3"]).click()
                self.driver.switch_to.default_content()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["registerFound"]).send_keys('10')
                self.find_element(By.XPATH,self.publishbid["serviceArea"]).click()
                self.find_element(By.XPATH,self.publishbid["china"]).click()
                self.find_element(By.XPATH,self.publishbid["ok4"]).click()
                self.find_element(By.XPATH,self.publishbid["detail"]).send_keys('good good study day day up')
                self.execute_js("var q=document.documentElement.scrollTop=10000")
                time.sleep(1)
                '''
                self.find_element(By.XPATH,self.publishbid["addown"]).click()
                self.find_element(By.XPATH,self.publishbid["ownname"]).send_keys(u'测试')
                self.find_element(By.XPATH,self.publishbid["ownjob"]).send_keys(u'测试')
                self.find_element(By.XPATH,self.publishbid["ownphone"]).send_keys(u'11112222345')
                '''
                self.find_element(By.XPATH,self.publishbid["selectOwn"]).click()
                self.find_element(By.XPATH,self.publishbid["selectOwn"]).send_keys(Keys.DOWN)
                self.find_element(By.XPATH,self.publishbid["selectOwn"]).send_keys(Keys.ENTER)
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["finish"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.publishbid["publishNow"]).click()
                time.sleep(2)
                self.find_element(By.XPATH,self.publishbid["publishedlist"]).click()
                time.sleep(1)
                name = self.find_element(By.XPATH,self.publishbid["publishbidname"]).text
                assert name == bidname
                logging.info("——招标发布成功——")
                return True
            else:
                logging.info("——发布招标失败——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkBasicSetting(self):
        self.find_element(By.XPATH,self.basicSetting["menu"]).click()
        try:
            assert self.switchToCompanyMsg()
            assert self.switchToOrg()
            assert self.switchToProjectSet()
            assert self.switchToFlagship()
            assert self.switchToAccountManage()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToCompanyMsg(self):
        logging.info("——检查公司资料界面——")
        try:
            if(self.is_element_exist(By.XPATH,self.basicSetting["logo"])):
                logging.info("——公司资料显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——公司资料显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToOrg(self):
        logging.info("——检查组织架构界面——")
        self.find_element(By.XPATH,self.basicSetting["org"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.basicSetting["tree"])):
                logging.info("——组织架构界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——组织架构界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToProjectSet(self):
        logging.info("——检查项目设置界面——")
        self.find_element(By.XPATH,self.basicSetting["itemSetting"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.basicSetting["newitem"])):
                logging.info("——项目设置界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——项目设置界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToFlagship(self):
        logging.info("——检查企业专区设置界面——")
        self.find_element(By.XPATH,self.basicSetting["flagship"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.basicSetting["enterMyship"])):
                logging.info("——企业专区设置界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——企业专区设置界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToAccountManage(self):
        logging.info("——检查管理所有账号界面——")
        self.find_element(By.XPATH,self.basicSetting["accountManage"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.basicSetting["transaccount"])):
                logging.info("——管理所有账号界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——管理所有账号界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkInspect(self):
        logging.info("——检查供应商评估界面——")
        self.find_element(By.XPATH,self.inspecttravel["menu"]).click()
        time.sleep(1)
        try:
            self.switchToInspectTravel()
            self.switchToInspectReport()
            self.switchToScoreList()
            self.switchToInspectSet()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToInspectTravel(self):
        logging.info("——新建考察行程——")
        try:
            self.find_element(By.XPATH,self.inspecttravel["create"]).click()
            time.sleep(1)
            inspectName ='考察行程测试%s'%(str(int(time.time())))
            self.find_element(By.XPATH,self.inspecttravel["title"]).send_keys(inspectName)
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["inspectSupplier"]).click()
            time.sleep(2)
            self.find_element(By.XPATH,self.inspecttravel["suppliername"]).send_keys(u"深圳市英拓贸易有限公司")
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["suppliername"]).send_keys(Keys.TAB)
            time.sleep(2)
            self.find_element(By.XPATH,self.inspecttravel["category"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["level1"]).click()
            self.find_element(By.XPATH,self.inspecttravel["level2"]).click()
            self.find_element(By.XPATH,self.inspecttravel["level3"]).click()
            self.find_element(By.XPATH,self.inspecttravel["ok"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["companyType"]).click()
            self.find_element(By.XPATH,self.inspecttravel["firstType"]).click()
            self.find_element(By.XPATH,self.inspecttravel["tax"]).click()
            self.find_element(By.XPATH,self.inspecttravel["firstTax"]).click()
            self.find_element(By.XPATH,self.inspecttravel["inspectDate"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["today"]).click()
            self.find_element(By.XPATH,self.inspecttravel["score"]).click()
            self.find_element(By.XPATH,self.inspecttravel["firstscore"]).click()
            self.find_element(By.XPATH,self.inspecttravel["team"]).click()
            self.find_element(By.XPATH,self.inspecttravel["teammember"]).click()
            self.find_element(By.XPATH,self.inspecttravel["save"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.inspecttravel["apply"]).click()
            time.sleep(1)
            name = self.find_element(By.XPATH,self.inspecttravel["verifyname"]).text
            if name.find(inspectName)!=-1:
                logging.info("——新建考察成功——")
                return True
            else:
                logging.info("——新建考察失败——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToInspectReport(self):
        logging.info("——检查考察报告界面——")
        self.find_element(By.XPATH,self.inspectreport["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.inspectreport["nodata"]) or self.is_element_exist(By.XPATH,self.inspectreport["haveDatas"])):
                logging.info("——考察报告界面显示正常——")
                if(self.is_element_exist(By.XPATH,self.inspectreport["haveDatas"])):
                    logging.info("——查看报告详情页面——")
                    self.find_element(By.XPATH,self.inspectreport["haveDatas"]).click()
                    self.switch_handle()
                    if(self.is_element_exist(By.XPATH,self.inspectreport["reportdetail"])):
                        logging.info("——报告详情页显示正常——")
                        self.driver.close()
                        self.switch_handle()
                        return True
                    else:
                        logging.info("——报告详情页显示有问题——")
                        self.driver.close()
                        self.switch_handle()
                        return False
                else:
                    logging.info("——没有报告可以查看——")
                    return True
            else:
                logging.info("——考察报告界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToScoreList(self):
        logging.info("——查看考察评分表库界面——")
        self.find_element(By.XPATH,self.inspectscorelist["menu"]).click()
        try:
            logging.info("——新建评分表——")
            self.find_element(By.XPATH,self.inspectscorelist["create"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.inspectscorelist["gradescore"]).click()
            time.sleep(1)
            title = "评分表测试%s"%(str(int(time.time())))
            self.find_element(By.XPATH,self.inspectscorelist["title"]).send_keys(title)
            self.find_element(By.XPATH,self.inspectscorelist["demension"]).send_keys('维度1')
            time.sleep(1)
            source1 = self.find_element(By.XPATH,self.inspectscorelist["options"])
            target1 = self.find_element(By.XPATH,self.inspectscorelist["content"])
            self.find_element(By.XPATH,self.inspectscorelist["options"]).click()
            time.sleep(1)
            self.drag_and_drop(source1,target1)
            time.sleep(1)
            self.find_element(By.XPATH,self.target["targetTitle"]).send_keys("考察评分表指标1")
            self.find_element(By.XPATH,self.target["option1"]).click()
            self.find_element(By.XPATH,self.target["option1"]).send_keys("100")
            self.find_element(By.XPATH,self.target["option1"]).click()
            self.find_element(By.XPATH,self.target["option2"]).send_keys("80")
            self.find_element(By.XPATH,self.target["option1"]).click()
            self.find_element(By.XPATH,self.target["option3"]).send_keys("60")
            self.find_element(By.XPATH,self.target["option1"]).click()
            self.find_element(By.XPATH,self.target["option4"]).send_keys("40")
            self.find_element(By.XPATH,self.target["option1"]).click()
            self.find_element(By.XPATH,self.target["option5"]).send_keys("0")
            time.sleep(1)
            source2 = self.find_element(By.XPATH,self.inspectscorelist["fillin"])
            target2 = self.find_element(By.XPATH,self.inspectscorelist["content"])
            self.drag_and_drop(source2,target2)
            time.sleep(1)
            self.find_element(By.XPATH,self.target["targetTitle"]).send_keys("考察评分表指标2")
            self.find_element(By.XPATH,self.target["standard"]).send_keys("good good study,day day up")
            self.find_element(By.XPATH,self.target["score"]).send_keys("20")
            time.sleep(1)
            self.find_element(By.XPATH,self.target["apply"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.target["ok"]).click()
            time.sleep(1)
            name = self.find_element(By.XPATH,self.inspectscorelist["scoretablename"]).text
            if(name == title):
                logging.info("——新建评分表成功——")
                logging.info("——删除评分表——")
                self.find_element(By.XPATH,self.inspectscorelist["delete"]).click()
                time.sleep(1)
                self.find_element(By.XPATH,self.target["ok"]).click()
                return True
            else:
                logging.info("——新建评分表失败——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToInspectSet(self):
        logging.info("——检查考察设置界面——")
        self.find_element(By.XPATH,self.inspectset["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.inspectset["scorelevel"])):
                logging.info("——考察设置界面显示正常——")
                return True
            else:
                logging.info("——考察设置界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg