from selenium.webdriver.common.by import By

from Base.base import Base
loc_click=By.ID, "com.android.settings:id/search"
loc_username=By.ID, "android:id/search_src_text"
loc_password=By.CLASS_NAME, "android.widget.ImageButton"
class PageLogin(Base):
    #点击搜索
    def page_click(self):
        self.base_click(loc_click)
    #输入内容
    def page_username(self,text):
        self.base_input(loc_username,text)
    #点击返回
    def page_password(self):
        self.base_click(loc_password)

