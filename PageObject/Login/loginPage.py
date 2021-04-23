__author__ = 'wuxj06'
#encoding=utf-8
from Common.BasePage import BasePage
from selenium.webdriver.common.by import By
import time
from Common import Logger,config
import logging

class LoginPage(BasePage):
    #登录相关元素

    def login(self,url,username,password):
        try:
            self.driver.get(url)
            time.sleep(1)
            self.find_element(By.XPATH,self.loginParam["logbtn"]).click()
            time.sleep(1)
            self.find_element(By.XPATH,self.loginParam["pwdlogin"]).click()
            self.find_element(By.XPATH,self.loginParam["mobile"]).send_keys(username)
            self.find_element(By.XPATH,self.loginParam["password"]).send_keys(password)
            time.sleep(1)
            self.find_element(By.XPATH,self.loginParam["login"]).click()
            time.sleep(2)
            if(self.is_element_exist(By.XPATH,self.backstage)):
                logging.info("登录成功")
                return True
            else:
                logging.info("登录失败")
                return False
        except Exception as msg:
            logging.info("异常原因：%s"%msg)
            raise msg

