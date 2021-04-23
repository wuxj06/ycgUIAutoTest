#encoding=utf-8
__author__ = 'wuxj06'
import pytest
from PageObject.Login.loginPage import LoginPage
from selenium import webdriver
from TestData import common_data as CD
import os
import allure

gdriver = None

@pytest.fixture
def init_driver():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.url)
    yield driver


@pytest.fixture(scope="class")
def init_supplier_login():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    loginpage = LoginPage(driver)
    loginpage.login(CD.url,CD.username_supplier,CD.password_supplier)
    yield  driver

@pytest.fixture(scope="class")
def init_dev_login():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    loginpage = LoginPage(driver)
    loginpage.login(CD.url,CD.username_dev,CD.password_supplier)
    yield  driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        with allure.step('添加失败截图...'):
            allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)