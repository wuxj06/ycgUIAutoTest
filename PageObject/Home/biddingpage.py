__author__ = 'wuxj06'
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from Common import Logger,config
import time
import MySQLdb

class BiddingPage(BasePage):

    def getItemId(self):
        logging.info("——获取最新发布的招标id——")
        db = MySQLdb.connect(host="139.196.98.138",port=63306,user="b2bmir_connect",passwd="IgJT5sk4XZKD",db="b2b_bidding",charset='utf8')
        cursor=db.cursor()
        cursor.execute("select uid from b2b_bidding.bid_announcements ORDER BY created_time desc LIMIT 1")
        uid = cursor.fetchone()[0]
        return uid

    def signUpbid(self):
        logging.info("——报名招标——")
        uid = self.getItemId()
        url = "https://zb.b2bmir.com/bidding-%s.html"%uid
        self.driver.get(url)
        time.sleep(2)
        try:
            self.find_element(By.XPATH,self.bid["signup"]).click()
            time.sleep(1)
            if(self.is_element_exist(By.XPATH,self.bid["closebtn"])):
                self.find_element(By.XPATH,self.bid["closebtn"]).click()
                time.sleep(1)
                logging.info("——报名前需要关注云采购微信公众号——")
                return True
            elif(self.is_element_exist(By.XPATH,self.bid["success"])):
                logging.info("——报名成功——")
                return True
            elif(self.is_element_exist(By.XPATH,self.bid["failmessage"])):
                logging.info("——报名失败，服务分类或其他条件不符合——")
                return True
            elif(self.is_element_exist(By.XPATH,self.bid["sorrytips"])):
                logging.info("——报名失败，权限不足——")
                return True
            elif(self.is_element_exist(By.XPATH,self.bid["dialog"])):
                logging.info("——报名需要跳转到采购门户——")
                self.find_element(By.XPATH,self.bid["dialog"]).click()
                self.switch_handle()
                if(self.is_element_exist(By.XPATH,self.bid["menhuBtn"])):
                    logging.info("——门户跳转正常——")
                    return True
                else:
                    logging.info("——门户跳转失败——")
                    return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg