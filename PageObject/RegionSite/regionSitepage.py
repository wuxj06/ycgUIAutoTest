__author__ = 'wuxj06'
#encoding=utf-8
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from Common import Logger,config
import logging

class RegionSitePage(BasePage):

    def checkHomePage(self):
        logging.info("——检查区域分站首页——")
        try:
            if(self.is_element_exist(By.XPATH,self.home["recommendlist"]) and self.is_element_exist(By.XPATH,self.home["materialprice"])):
                logging.info("——区域分站首页显示正常——")
                return True
            else:
                logging.info("——区域分站首页显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecommendSupplier(self):
        logging.info("——检查推荐供应商页面——")
        self.find_element(By.XPATH,self.recommend["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.recommend["companylist"])):
                logging.info("——推荐供应商页面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——推荐供应商页面显示有问题——")
                self.driver.close()
                self.switch_handle()
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkPrice(self):
        logging.info("——检查区域信息价界面——")
        self.find_element(By.XPATH,self.price["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.price["material"])):
                logging.info("——区域信息价界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——区域信息价界面显示有问题——")
                self.driver.close()
                self.switch_handle()
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecruitAndBid(self):
        logging.info("——检查招募招标界面——")
        self.find_element(By.XPATH,self.recruitAndbid["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.recruitAndbid["list"])):
                logging.info("——招募招标界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——招募招标界面显示有问题——")
                self.driver.close()
                self.switch_handle()
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkItemCase(self):
        logging.info("——检查项目案例界面——")
        self.find_element(By.XPATH,self.itemCase["menubar"]).click()
        self.switch_handle()
        try:
            if(self.is_element_exist(By.XPATH,self.itemCase["content"])):
                logging.info("——项目案例界面显示正常——")
                self.driver.close()
                self.switch_handle()
                return True
            else:
                logging.info("——项目案例界面显示有问题——")
                self.driver.close()
                self.switch_handle()
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkbusinessAndwinBid(self):
        logging.info("——检查入库和中标界面——")
        self.find_element(By.XPATH,self.businessAndwinBid["menubar"]).click()
        self.switch_handle()
        if(self.is_element_exist(By.XPATH,self.businessAndwinBid["business"])):
            logging.info("——入库和中标界面显示正常——")
            return True
        else:
            logging.info("——入库和中标界面显示有问题——")
            self.driver.close()
            return False