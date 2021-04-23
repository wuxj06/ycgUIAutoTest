#encoding=utf-8
__author__ = 'wuxj06'
from PageObject.Login.loginPage import LoginPage
from TestData import common_data as CD
import logging
import pytest
import allure

@pytest.mark.usefixtures('init_driver')
class Test_Login:

    @pytest.mark.smoke
    @allure.feature(u'登录')
    @allure.story(u'供应商登录')
    def test_login_supplier(self,init_driver):
        login = LoginPage(init_driver)
        assert login.login(CD.url,CD.username_supplier,CD.password_supplier)


    @pytest.mark.smoke
    @allure.feature(u'登录')
    @allure.story(u'开发商登录')
    def test_login_dev(self,init_driver):
        login = LoginPage(init_driver)
        assert login.login(CD.url,CD.username_dev,CD.password_supplier)
