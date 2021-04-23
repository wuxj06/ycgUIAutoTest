__author__ = 'wuxj06'
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Common import config
import win32gui
import win32con
import time
import pyautogui
import allure


class BasePage:

    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def element_wait(self,by,locator,wait_time=10):
        if by not in [By.ID,By.XPATH,By.ID,By.XPATH,By.LINK_TEXT,By.CSS_SELECTOR,By.CLASS_NAME,By.TAG_NAME,By.PARTIAL_LINK_TEXT]:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        try:
            WebDriverWait(self.driver,wait_time,0.5).until(EC.presence_of_element_located((by,locator)))
            return True
        except TimeoutException:
            return False

    #查找单个元素
    def  find_element(self,by,locator,wait_time=8):
        self.element_wait(by,locator,wait_time)
        return self.driver.find_element(by,locator)

    #查找多个元素
    def  find_elements(self,by,locator,wait_time=8):
        self.element_wait(by,locator,wait_time)
        return self.driver.find_elements(by,locator)

    #判断元素是否存在
    def is_element_exist(self,by,locator):
        try:
            self.find_element(by,locator)
            return True
        except:
            return False

    #上传文件
    def upload_file(self,style):
        dialog = win32gui.FindWindow("#32770","打开")
        ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
        comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
        edit = win32gui.FindWindowEx(comboBox,0,'Edit',None)
        button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")
        filepath = config.attach_dir + style
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)

    #等待
    def implicitly_wait(self,time=5):
        self.driver.implicitly_wait(time)


    #切换到最新打开的窗口
    def switch_handle(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        time.sleep(2)

    #执行js脚本
    def execute_js(self,js):
        self.driver.execute_script(js)
        time.sleep(0.5)

    #滚动查找
    def element_scrollIntoView(self,ele):
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        time.sleep(0.5)

    #拖拽元素,因为试了用selenium自带的拖拽方法没有效果，所以这里用pyautogui试试
    def drag_and_drop(self,source,target):
        pyautogui.moveTo(source.location['x']+20,source.location['y']+125)
        pyautogui.dragTo(target.location['x']+20,target.location['y']+125,duration=1)


