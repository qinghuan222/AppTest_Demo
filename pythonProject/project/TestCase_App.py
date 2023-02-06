# -*-coding:utf-8 -*-
# import sys
# from importlib import reload
import os
from appium import webdriver
import time
from selenium.webdriver.common.by import By
import unittest
import logging
import HTMLTestRunner
from pythonProject.project.Login import Login_app

# 日志输出文档
# reload(sys)
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + r'\..') # 返回脚本的路径
# logging.basicConfig(level=logging.DEBUG,
#      format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#      datefmt='%a, %d %b %Y %H:%M:%S',
#      filename='log_test.log',
#      filemode='w')
# logger.setLevel(level=logging.DEBUG)
# logger = logging.getLogger()

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)  # 设置日志级别,只打印该级别以上的日志
console = logging.StreamHandler()  # 创建一个StreamHandler，用于输出到控制台
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 自定义输出格式
console.setFormatter(formatter)  # 绑定格式
logger.addHandler(console)


class DemoAppTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',  # 设备类型；
            'platformVersion': '10',  # 设备的类型的版本号
            'deviceName': '597331de',  # 设备的名称
            'appPackage': 'com.app.huibo',  # 的app包名；
            'appActivity': 'module.main.WelcomeActivity',  #activity名
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # logger.info("启动App，开始执行用例....")


    def tearDown(self):
        self.driver.quit()

    def test_appcom_login(self):
        logger.info("用例名-企业登陆，测试数据：账号：15000000033，密码：a123456")
        Login_app(self.driver).login1("15000000033", "a123456")

    def test_a_appcom_invite_resume(self):
        logger.info("用例名-邀请面试")
        Login_app(self.driver).login1("15000000033", "a123456")
        # 搜索栏点击
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_titleSearch").send_keys("19535133")     #搜索简历编号
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_searchResume").click()      #点击搜索
        time.sleep(2)
        # 点击简历进入简历详情页
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/ll_mantle").click()       #蒙层点击
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_invite").click()       #邀请按钮点击啊
        time.sleep(5)
        # 面试日期选择栏点击
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]").click()
        time.sleep(2)
        # 面试日期选择
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.view.View[2]/android.view.View[1]/android.widget.ListView/android.widget.Button[2]").click()
        time.sleep(2)
        # 选择日期后点击"确定"按钮
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.Button[2]").click()
        time.sleep(2)
         # 面试时间选择
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[15]").click()
        time.sleep(2)
        # 面试时间确定
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.Button[2]").click()
        time.sleep(2)
        # 点击邀请面试按钮
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View").click()
        time.sleep(2)

    def test_appcom_send_message(self):
        logger.info("用例名-发送消息")
        Login_app(self.driver).login1("15000000033", "a123456")
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_tab2").click()     #点击互动icon
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_iGotItNext").click()       #蒙层点击
        time.sleep(2)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_iGotIt").click()       #蒙层点击
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/rl_item").click()      #会话点击
        time.sleep(3)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_inputTextToChat").send_keys("企业发送测试消息")     #输入文案
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_send").click()      #发送按钮
        time.sleep(1)

    def test_appcom_job(self):
        logger.info("用例名-发布职位")
        Login_app(self.driver).login1("15000000033", "a123456")
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        # self.driver.find_element(By.LINK_TEXT,"发布职位").click()
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_jobName").send_keys("ui自动化测试回归-勿投递")        #职位名
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_jobDescription").click()    #职位描述点击
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_content").send_keys("ui自动化测回归，发布职位-该操作为编写职位描述，省略。。。。。。。。。。。。。")     #编辑职位描述
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_basicUiTitleRightName").click()     #职位描述保存按钮
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_jobCategory").click()     #职位类别选项点击
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_jobCategorySelectSearch").send_keys("自动化测试")     #职位类别搜索
        time.sleep(3)
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.RelativeLayout").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_recruitNumber").send_keys("2")     #招聘人数
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_education").click()     #学历点击
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_submit").click()     #学历确认
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_age").click()     #年龄选择
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_submit").click()     #年龄确定
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/rl_salary").click()     #薪资待遇点击
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_minSalary").send_keys("1111")     #最低薪资
        self.driver.find_element(By.ID,"com.app.huibo:id/et_maxSalary").send_keys("2222")     #最高薪资
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_payDay").click()     #发薪日期选择
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_submit").click()     #发薪日期确定
        time.sleep(2)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_submit").click()  # 薪资编辑保存
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        self.driver.swipe(x1,y1,x1,y2,500)
        '''
        向上滑动操作
        '''
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_jobExperience").click()     #工作经验选择
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_submit").click()     #工作经验确定
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_jobLabel").click()     #职位特点点击
        # 职位特点选择
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[11]/android.widget.TextView").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_positionLabelSure").click()        #职位特点保存
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_positionLevel").click()     #职位级别选择
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_submit").click()     #职位级别确认
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_welfare").click()     #福利待遇点击
        # 福利待遇确认
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_welfareSure").click()     #福利待遇保存
        time.sleep(1)
        '''
        向上滑动操作
        '''
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        self.driver.swipe(x1, y1, x1, y2, 500)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_holidaysWorkingHours").click()     #假期及上班时间点击
        time.sleep(1)
        # 假期及上班时间选择
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_holidayWorkTimeSure").click()   #假期及上班时间保存
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_placeOfWork").click()       #工作地点点击
        time.sleep(8)
        #  工作地点选择
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.view.ViewGroup/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]").click()
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/btn_sure").click()     #工作地点保存
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_switchFastRecruitType").click()     # 切换为普通职位
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_ok").click()       #弹窗确定按钮
        l = self.driver.get_window_size()
        x1 = l['width'] * 0.5
        y1 = l['height'] * 0.75
        y2 = l['height'] * 0.25
        self.driver.swipe(x1, y1, x1, y2, 100)
        '''
        向上滑动操作
        '''
        self.driver.find_element(By.ID,"com.app.huibo:id/btn_publishNow").click()


    def test_app_login(self):
        logger.info("用例名-求职者登陆，测试数据：账号：19000000000，密码：a123456")
        Login_app(self.driver).login("19000000000", "a123456")


    def test_app_homesearch(self):
        # logger.info("执行账号登陆操作")
        Login_app(self.driver).login("19000000000","a123456")
        logger.info("用例名-搜索职位-查看职位详情页")
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_search").click()  #搜索框
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_searchKey").send_keys("测试")  #输入搜索关键词
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_search").click()  #点击搜索
        time.sleep(8)  # 注意数据拉取时间
        self.driver.find_element(By.ID, "com.app.huibo:id/iv_ok").click()  #蒙层点击
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"android.view.ViewGroup").click()     #点击职位
        time.sleep(5)
        self.driver.find_element(By.ID,"com.app.huibo:id/iv_back").click()  #返回icon
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/iv_back").click()  #返回icon
        time.sleep(1)
        self.driver.find_element(By.ID,"com.app.huibo:id/iv_back").click()  #返回icon


    def test_app_jobCategory(self):
        # logger.info("执行账号登陆操作,账号：19000000000，密码：a123456")
        Login_app(self.driver).login("19000000000", "a123456")
        logger.info("用例名-修改求职意向-期望职位")
        self.driver.find_element(By.ID, "com.app.huibo:id/iv_editRecommendCategory").click()   #点击"+"icon
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_jobCategory").click()  #点击期望职位
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME,"android.widget.TextView").click()  #选择销售经理
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_selectJobCategorySure").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "com.app.huibo:id/tv_save").click()  #保存按钮
        time.sleep(1)


    def test_app_deliver_resume(self):
        Login_app(self.driver).login("19000000000", "a123456")
        logger.info("用例名-投递简历")
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_textCompany").click()  #点击底部banner公司icon
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_companySearch").click() #点击搜索
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_searchKey").send_keys("小跳蛙")    #输入公司名
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_search").click()    #点击搜索
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_position").click()  #点击在招职位
        time.sleep(2)
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/androidx.viewpager.widget.ViewPager/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]").click()    #点击职位
        time.sleep(2)
        '''
        注意职位是否投递过，更新上一步元素定位，可在第一步更换账号[2]
        '''
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_deliverResume").click()
        time.sleep(5)

    def test_app_send_message(self):
        logger.info("用例名-发送消息")
        Login_app(self.driver).login("19000000000", "a123456")
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_textMessage").click()   #点击底部banner消息icon
        time.sleep(5)
        '''
        注意元素定位，会话列表元素定位可能会出问题,[2]
        '''
        self.driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[2]").click()     #点击消息列表会话
        time.sleep(3)
        self.driver.find_element(By.ID,"com.app.huibo:id/et_inputTextToChat").send_keys("测试消息")   #输入消息文案
        time.sleep(2)
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_send").click()  #点击发送
        time.sleep(2)

    def test_app_agr_invite(self):
        logger.info("接受面试邀请")
        Login_app(self.driver).login("19000000000","a123456")
        self.driver.find_element(By.ID,"com.app.huibo:id/tv_acceptInterview").click()
        time.sleep(5)
        self.driver.find_element(By.ID,"com.app.huibo:id/bt_ok").click()


if __name__ == '__main__':
    # unittest.main()
    # 实例化
    testunit = unittest.TestSuite()
    # 加载用例
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(DemoAppTest))
    # 当前文件夹路径
    report_path = os.path.dirname(os.path.abspath(__file__) + r'\..')
    # 测试报告地址
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    # 报告详情
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 执行用例
    runner.run(testunit)
    # 关闭报告
    fp.close()