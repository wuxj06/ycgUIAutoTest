__author__ = 'wuxj06'
#encoding=utf-8
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from Common import Logger,config
import logging

class ServerTypeDetailPage(BasePage):


    def checkHomePage(self):
        logging.info("——检查服务分类首页——")
        try:
            if(self.is_element_exist(By.XPATH,self.home["recommendList"]) and self.is_element_exist(By.XPATH,self.home["wikilist"])):
                logging.info("——服务分类首页显示正常——")
                return True
            else:
                logging.info("——服务分类首页显示有问题——")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg

    def checkRecommentSupplier(self):
        logging.info("——检查推荐供应商界面——")
        self.find_element(By.XPATH,self.recommend["menubar"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.recommend["supplierList"])):
                logging.info("——推荐供应商显示正常——")
                return True
            else:
                logging.info("——推荐供应商界面显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            self.driver.save_screenshot(config.img_dir+time.strftime("%Y%m%d.%H.%M.%S")+".png")
            raise msg

    def checkRecruitAndBid(self):
        logging.info("——检查招募招标界面——")
        self.find_element(By.XPATH,self.recruitAndBid["menubar"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.recruitAndBid["list"])):
                logging.info("——招募招标界面显示正常——")
                return True
            else:
                logging.info("——招募招标界面显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            self.driver.save_screenshot(config.img_dir+time.strftime("%Y%m%d.%H.%M.%S")+".png")
            raise msg

    def checkProjectCase(self):
        logging.info("——检查项目案例界面——")
        self.find_element(By.XPATH,self.projectCase["menubar"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.projectCase["caselist"])):
                logging.info("——项目案例界面显示正常——")
                return True
            else:
                logging.info("——项目案例界面显示有问题——")
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            self.driver.save_screenshot(config.img_dir+time.strftime("%Y%m%d.%H.%M.%S")+".png")
            raise msg

    def checkStorageAndWinbid(self):
        logging.info("——检查入库和中标界面——")
        self.find_element(By.XPATH,self.storageandwinbid["menubar"]).click()
        time.sleep(1)
        try:
            if(self.is_element_exist(By.XPATH,self.storageandwinbid["storagelist"])):
                logging.info("——最新成功入库界面显示正常——")
                self.find_element(By.XPATH,self.storageandwinbid["winbidbar"]).click()
                time.sleep(1)
                if(self.is_element_exist(By.XPATH,self.storageandwinbid["winbidlist"])):
                    logging.info("——最新中标界面显示正常——")
                    return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            self.driver.save_screenshot(config.img_dir+time.strftime("%Y%m%d.%H.%M.%S")+".png")
            raise msg
