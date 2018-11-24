from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver
    #查找元素
    def base_find_element(self,loc,timeout=10,poll=0.5):
      return  WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x : x.find_element(*loc))
    #点击元素  封装
    def base_click(self,loc):
        self.base_find_element(loc).click()
    #输入方法 封装
    def base_input(self,loc,text):
        #查找元素
        el=self.base_find_element(loc)
        #清除元素
        el.clear()
        #输入内容
        el.send_keys(text)