__author__ = 'wuxj06'
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from Common import Logger,config
import time
from PageObject.Home.homepage import HomePage

class SupplierBackStage(BasePage):
    #工作台
    workstation ={}


    def checkWorkStation(self):
        hp = HomePage(self.driver)
        hp.switchToBackStage()
        logging.info("——检查工作台界面——")
        try:
            if(self.is_element_exist(By.XPATH,self.workstation["closebtn"])):
                self.find_element(By.XPATH,self.workstation["closebtn"]).click()
                time.sleep(1)
            if(self.is_element_exist(By.XPATH,self.workstation["dataBox"]) and self.is_element_exist(By.XPATH,self.workstation["message"]) and self.is_element_exist(By.XPATH,self.workstation["recommend"])):
                logging.info("——工作台界面显示正常——")
                self.find_element(By.XPATH,self.workstation["view"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.workstation["viewlist"])):
                    logging.info("——工作台-浏览记录界面显示正常")
                    self.driver.close()
                    self.switch_handle()
                self.find_element(By.XPATH,self.workstation["myorder"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.workstation["orderlist"]) or self.is_element_exist(By.XPATH,self.workstation["nodata"])):
                    logging.info("——工作台-发票订单界面显示正常——")
                    self.driver.close()
                    self.switch_handle()
                time.sleep(2)
                return True
            else:
                logging.info("——工作台界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            raise msg


    #个人设置
    def checkUserSetting(self):
        logging.info("——检查个人设置界面——")
        self.find_element(By.XPATH,self.usersetting["setting"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.usersetting["name"])):
                logging.info("——个人设置-个人资料界面显示正常——")
                self.find_element(By.XPATH,self.usersetting["accountsafe"]).click()
                time.sleep(1)
                if(self.is_element_exist(By.XPATH,self.usersetting["msglist"])):
                    logging.info("——个人设置-账号安全界面显示正常——")
                    self.find_element(By.XPATH,self.usersetting["reauth"]).click()
                    time.sleep(1)
                    if(self.is_element_exist(By.XPATH,self.usersetting["companyname"])):
                        logging.info("——认证界面显示正常——")
                        self.driver.close()
                        self.switch_handle()
                        return True
            else:
                logging.info("——个人设置界面显示有问题——")
                self.driver.close()
                self.switch_handle()
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    #营销数据统计
    def checkDatacount(self):
        logging.info("——检查营销数据统计界面——")
        self.find_element(By.XPATH,self.datacount["menu"]).click()
        time.sleep(2)
        try:
            if(self.is_element_exist(By.XPATH,self.datacount["exposureTimes"]) and self.is_element_exist(By.XPATH,self.datacount["pv"]) and self.is_element_exist(By.XPATH,self.datacount["visitor"]) and self.is_element_exist(By.XPATH,self.datacount["exposureChannel"]) and self.is_element_exist(By.XPATH,self.datacount["conformbussiness"]) and self.is_element_exist(By.XPATH,self.datacount["recommendBussiness"])):
                logging.info("——营销数据统计界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——营销数据统计界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            raise msg

    def checkDataAnalysis(self):
        logging.info("——检查营销数据分析界面——")
        self.find_element(By.XPATH,self.dataAnalysis["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.dataAnalysis["maplist"])):
                logging.info("——营销数据分析界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——营销数据分析界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkMessage(self):
        logging.info("——检查供应商通知界面——")
        self.find_element(By.XPATH,self.message["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.message["container"])):
                logging.info("——供应商通知界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——供应商通知界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkSignUp(self):
        logging.info("——检查待报名界面——")
        self.find_element(By.XPATH,self.signup["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.signup["firstItem"])):
                logging.info("——待报名界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——待报名界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkMybidding(self):
        logging.info("——检查我的招标界面——")
        self.find_element(By.XPATH,self.mybidding["menu"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.mybidding["close"])):
                self.find_element(By.XPATH,self.mybidding["close"]).click()
            if(self.is_element_exist(By.XPATH,self.mybidding["filter"])):
                logging.info("——我的招标界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——我的招标界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkMyrecruit(self):
        logging.info("——检查我的招募界面——")
        self.find_element(By.XPATH,self.myrecruit["menu"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.myrecruit["close"])):
                self.find_element(By.XPATH,self.myrecruit["close"]).click()
            if(self.is_element_exist(By.XPATH,self.myrecruit["statuBar"])):
                logging.info("——我的招募界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——我的招募界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecruitApply(self):
        logging.info("——检查主动申请入库界面——")
        self.find_element(By.XPATH,self.recruitApply["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.recruitApply["content"])):
                logging.info("——主动申请入库界面显示正常——")
                self.find_elements(By.XPATH,self.recruitApply["applyBtn"])[0].click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.recruitApply["doApply"]) or self.is_element_exist(By.XPATH,self.recruitApply["bar"])):
                    logging.info("——开发商入库界面正常打开——")
                    self.driver.close()
                    self.switch_handle()
                    return True
                else:
                    logging.info("——开发商入库界面显示有问题——")
                    
                    return False
            else:
                logging.info("——主动申请入库界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkMenhumanage(self):
        logging.info("——检查采购门户管理界面——")
        self.find_element(By.XPATH,self.menhumanage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.menhumanage["firstDev"])):
                logging.info("——采购门户管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——采购门户管理界面显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            return False


    def checkRegistrationindex(self):
        logging.info("——检查资格预审界面——")
        self.find_element(By.XPATH,self.registrationindex["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.registrationindex["table"])):
                logging.info("——资格预审界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——资格预审界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkBuscard(self):
        logging.info("——检查名片交换界面——")
        self.find_element(By.XPATH,self.buscard["menu"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.buscard["mycard"])):
                self.find_element(By.XPATH,self.buscard["mycard"]).click()
                time.sleep(1)
                if(self.is_element_exist(By.XPATH,self.buscard["img"])):
                    self.find_element(By.XPATH,self.buscard["cancel"]).click()
                    time.sleep(1)
                    self.find_element(By.XPATH,self.buscard["moreChange"]).click()
                    time.sleep(1)
                    if(self.is_element_exist(By.XPATH,self.buscard["listcontent"])):
                        logging.info("——名片交换界面显示正常——")
                        time.sleep(2)
                        return True
            else:
                logging.info("——名片交换界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkStorage(self):
        logging.info("——检查入库管理界面——")
        self.find_element(By.XPATH,self.storage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.storage["tablist"])):
                logging.info("——入库管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——入库管理界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkOnlinemeeting(self):
        logging.info("——检查我的对接会界面——")
        self.find_element(By.XPATH,self.onlinemeeting["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.onlinemeeting["table"])):
                logging.info("——我的对接会界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——我的对接会界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkSupplierArchive(self):
        logging.info("——检查企业档案界面——")
        self.find_element(By.XPATH,self.supplierArchive["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.supplierArchive["name"])):
                logging.info("——企业档案界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——企业档案界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkWinbid(self):
        logging.info("——检查中标发布界面——")
        time.sleep(1)
        self.find_element(By.XPATH,self.winbid["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.winbid["button"])):
                logging.info("——中标发布界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——中标发布界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkCaseManage(self):
        logging.info("——检查案例管理界面——")
        self.find_element(By.XPATH,self.caseManage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.caseManage["addCase"])):
                logging.info("——案例管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——案例管理界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkProductManage(self):
        logging.info("——检查产品管理界面——")
        self.find_element(By.XPATH,self.productManage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.productManage["addProduct"])):
                logging.info("——产品管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——产品管理界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkArticleList(self):
        logging.info("——检查企业风采界面——")
        self.find_element(By.XPATH,self.articleList["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.articleList["addArticle"])):
                logging.info("——企业风采界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——企业风采界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkShowroom(self):
        logging.info("——检查展厅轮播图界面——")
        self.find_element(By.XPATH,self.showroom["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.showroom["upload"])):
                logging.info("——展厅轮播图界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——展厅轮播图界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkAdmanage(self):
        logging.info("——检查广告位管理界面——")
        self.find_element(By.XPATH,self.admanage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.admanage["text"])):
                logging.info("——广告位管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——广告位管理界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkTargetedPromotion(self):
        logging.info("——检查定向推广界面——")
        self.find_element(By.XPATH,self.targetedPromotion["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.targetedPromotion["button"])):
                logging.info("——定向推广界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——定向推广界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkDomain(self):
        logging.info("——检查二级域名界面——")
        self.find_element(By.XPATH,self.domain["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.domain["button"])):
                logging.info("——二级域名界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——二级域名界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkAccountManage(self):
        logging.info("——检查账号管理界面——")
        self.find_element(By.XPATH,self.accountManage["menu"]).click()
        try:
            if(self.is_element_exist(By.XPATH,self.accountManage["firstAccount"])):
                logging.info("——账号管理界面显示正常——")
                time.sleep(2)
                return True
            else:
                logging.info("——账号管理界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            

    def checkCompanyHall(self):
        logging.info("——检查企业展厅——")
        self.find_element(By.XPATH,self.myHall["menu"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.myHall["navigation"]) or self.is_element_exist(By.XPATH,self.myHall["companyname"])):
                logging.info("——企业展厅界面显示正常——")
                time.sleep(2)
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——企业展厅界面显示有问题——")
                
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            