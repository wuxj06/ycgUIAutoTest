__author__ = 'wuxj06'
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from Common import Logger,config
import time

class HomePage(BasePage):

    def checkHomePage(self):
        logging.info("——检查首页显示——")
        try:
            if(self.is_element_exist(By.XPATH,self.home["type"]) and self.is_element_exist(By.XPATH,self.home["newbidding"]) and self.is_element_exist(By.XPATH,self.home["newrecruit"]) and self.is_element_exist(By.XPATH,self.home["developerTop"])):
                logging.info("——行业分类模块显示正常——")
            else:
                logging.info("——行业分类模块显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg
        try:
            if(self.is_element_exist(By.XPATH,self.home["brand"])):
                logging.info("——品牌覆盖模块显示正常——")
            else:
                logging.info("——品牌覆盖模块显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg
        try:
            if(self.is_element_exist(By.XPATH,self.home["activity"])):
                logging.info("——线下活动模块显示正常——")
            else:
                logging.info("——线下活动模块显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg
        try:
            if(self.is_element_exist(By.XPATH,self.home["activity"])):
                logging.info("——人脉链接模块显示正常——")
                return True
            else:
                logging.info("——人脉链接模块显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkSearch(self):
        logging.info("——检查大数据寻源界面——")
        try:
            self.find_element(By.XPATH,self.search["menubar"]).click()
            self.switch_handle()
            assert self.switchToSupplierSearch()
            assert self.switchToBidAndRecruitSearch()
            assert self.switchToDeveloperSearch()
            assert self.switchToNewsSearch()
            self.driver.close()
            return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg


    def switchToSupplierSearch(self):
        logging.info("——检查供应商寻源界面——")
        try:
            if(self.is_element_exist(By.XPATH,self.search["suppliername"])):
                logging.info("——供应商寻源界面显示正常——")
                self.find_element(By.XPATH,self.search["suppliername"]).click()
                logging.info("——打开一个供应商——")
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.search["companymessage"]) or self.is_element_exist(By.XPATH,self.search["diamondCompany"])):
                    logging.info("——供应商详情页显示正常——")
                    self.driver.close()
                    self.switch_handle()
                    return True
            else:
                logging.info("——供应商寻源界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToBidAndRecruitSearch(self):
        logging.info("——检查招标招募寻源界面——")
        self.find_element(By.XPATH,self.search["procurement"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.search["firstItemName"])):
                logging.info("——招标招募寻源界面显示正常——")
                self.find_element(By.XPATH,self.recruit["recruitfilter"]).click()
                logging.info("——打开一个招募——")
                self.find_element(By.XPATH,self.recruit["firstrecruit"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.recruit["recuritname"])):
                    logging.info("——招募详情页显示正常——")
                    self.driver.close()
                    self.switch_handle()
                else:
                    logging.info("——招募详情页显示有问题")
                self.find_element(By.XPATH,self.bidannouncement["bidfilter"]).click()
                logging.info("——打开一个招标——")
                self.find_element(By.XPATH,self.bidannouncement["firstbid"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.bidannouncement["bidname"])):
                    logging.info("——招标详情页显示正常——")
                    self.driver.close()
                    self.switch_handle()
                else:
                    logging.info("——招标详情页显示有问题——")
                return True
            else:
                logging.info("——招标招募寻源界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToDeveloperSearch(self):
        logging.info("——检查开发商寻源界面——")
        self.find_element(By.XPATH,self.search["developer"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.search["developername"])):
                logging.info("——开发商寻源界面显示正常——")
                return True
            else:
                logging.info("——开发商寻源界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToNewsSearch(self):
        logging.info("——检查资讯百科界面——")
        self.find_element(By.XPATH,self.search["news"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.search["content"])):
                logging.info("——资讯百科界面显示正常——")
                return True
            else:
                logging.info("——资讯百科界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecruitAndBidding(self):
        logging.info("——检查招募招标界面——")
        self.switch_handle()
        self.find_element(By.XPATH,self.recruitandbid["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.recruitandbid["demand"]) and self.is_element_exist(By.XPATH,self.recruitandbid["toplist"]) and self.is_element_exist(By.XPATH,self.recruitandbid["winbidlist"]) and self.is_element_exist(By.XPATH,self.recruitandbid["lastedBid"])):
                logging.info("——招募招标界面显示正常——")
                self.driver.close()
                return True
            else:
                logging.info("——招募招标界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkSettledCompany(self):
        logging.info("——检查入驻企业界面——")
        self.switch_handle()
        self.find_element(By.XPATH,self.settledCompany["menubar"]).click()
        self.find_element(By.XPATH,self.settledCompany["supplier"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.settledCompany["demand"])):
                logging.info("——入驻供应商界面显示正常——")
                self.find_element(By.XPATH,self.settledCompany["menubar"]).click()
                self.find_element(By.XPATH,self.settledCompany["developer"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.settledCompany["developername"])):
                    logging.info("——入驻开发商界面显示正常——")
                    return True
            else:
                logging.info("——招募招标界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkCaizhaoStation(self):
        logging.info("——检查采招平台界面——")
        self.find_element(By.XPATH,self.caizhao["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.caizhao["developer"])):
                logging.info("——采招平台界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——采招平台界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkZone(self):
        logging.info("——检查行业专区界面——")
        self.find_element(By.XPATH,self.zone["menubar"]).click()
        self.find_element(By.XPATH,self.zone["building"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.zone["hotnews"]) and self.is_element_exist(By.XPATH,self.zone["newbusiness"])):
                logging.info("——行业专区界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——行业专区界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkZixun(self):
        logging.info("——检查资讯界面——")
        self.find_element(By.XPATH,self.zixun["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.zixun["news"])):
                logging.info("——资讯界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——资讯界面显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def switchToServerDetail(self):
        logging.info("——打开服务分类详情页——")
        self.find_element(By.XPATH,self.serverType).click()
        self.switch_handle()

    def switchToRegionSite(self):
        logging.info("——打开区域分站页面——")
        self.find_element(By.XPATH,self.region["menubar"]).click()
        time.sleep(1)
        self.find_element(By.XPATH,self.region["shanghai"]).click()
        self.switch_handle()

    def switchToBackStage(self):
        self.find_element(By.XPATH,self.home['backstage']).click()
        time.sleep(2)