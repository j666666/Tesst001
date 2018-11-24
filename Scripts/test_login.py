import os,sys

import allure
import pytest

sys.path.append(os.getcwd())
from Base.get_driver import get_driver
from Page.page_login import PageLogin

class TestLogin():
    # 初始化方法
    @pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    @allure.step("执行开始操作!")
    def setup_class(self):
        allure.attach("描述","登录成功!")
        #实例化PageLogin
        self.login=PageLogin(get_driver())
    #结束方法
    @allure.step("执行推出操作!")
    def teardown_class(self):
        allure.attach("描述", "退出成功!")
        self.login.driver.quit()

    #测试方法
    def test_login(self,text="WLAN"):
        #点击搜索
        self.login.page_click()
        #输入内容
        self.login.page_username(text)
        #点击返回
        self.login.page_password()




