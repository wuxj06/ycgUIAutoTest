__author__ = 'wuxj06'
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import logging
from Common import Logger,config
import time
import MySQLdb

class RecruitPage(BasePage):

    def getItemId(self):
        logging.info("——获取最新发布的招募id——")
        db = MySQLdb.connect(host="139.196.98.138",port=63306,user="b2bmir_connect",passwd="IgJT5sk4XZKD",db="b2b_bidding",charset='utf8')
        cursor=db.cursor()
        cursor.execute("select item_id from b2b_bidding.bid_recruit_item ORDER BY create_time desc LIMIT 1")
        item_id = cursor.fetchone()[0]
        return item_id

    def signUpRecruit(self):
        logging.info("——报名招募——")
        itemid = self.getItemId()
        url = "https://zm.b2bmir.com/detail-%s.html"%itemid
        self.driver.get(url)
        time.sleep(6)
        try:
            self.find_element(By.XPATH,self.signup).click()
            time.sleep(1)
            if(self.is_element_exist(By.XPATH,self.successmessage)):
                logging.info("——报名成功——")
                return True
            elif(self.is_element_exist(By.XPATH,self.failmessage)):
                logging.info("——报名失败，服务分类或其他条件不符合——")
                return True
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            
            raise msg