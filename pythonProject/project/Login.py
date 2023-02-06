import time
from selenium.webdriver.common.by import By
#求职者/企业登陆方法封装


class Login_app():

    def __init__(self,driver):
        self.driver = driver

    def click_ok(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_ok").click(),time.sleep(2)  #隐私协议弹窗

    def btn_jobSeeker(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/btn_jobSeeker").click(),time.sleep(3)  #点击我要找工作

    def login_type(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_loginType").click()    #选择登陆方式-账号登陆

    def input_username(self,username):
        self.driver.find_element(By.ID, "com.app.huibo:id/et_username").send_keys(username),time.sleep(1)   #输入求职者账号

    def input_pwd(self,pwd):
        self.driver.find_element(By.ID, "com.app.huibo:id/et_password").send_keys(pwd),time.sleep(1)    #输入求职者账号密码

    def click_btn(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/cb_pwProtocol").click(),time.sleep(1)     #勾选隐私协议

    def click_bt_login(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/btn_login").click(),time.sleep(2)     #登陆按钮

    # 企业
    def btn_boss(self):
        self.driver.find_element(By.ID, "com.app.huibo:id/btn_boss").click(), time.sleep(3)     #点击我要招人

    def input_userName(self,userName):
        self.driver.find_element(By.ID, "com.app.huibo:id/et_userName").send_keys(userName),time.sleep(1)       #输入企业账号

    def input_userPwd(self,userPwd):
        self.driver.find_element(By.ID, "com.app.huibo:id/et_userPwd").send_keys(userPwd),time.sleep(1)     #输入企业账号密码

    def noticeimg(self):
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_close").click(),time.sleep(1)

    # 求职者登陆
    def login(self,username,pwd):
        self.click_ok()
        self.btn_jobSeeker()
        self.login_type()
        self.input_username(username)
        self.input_pwd(pwd)
        self.click_btn()
        self.click_bt_login()

    # 企业登陆
    def login1(self,userName,userPwd):
        self.click_ok()
        self.btn_boss()
        self.input_userName(userName)
        self.input_userPwd(userPwd)
        self.click_btn()
        self.click_bt_login()
        self.noticeimg()