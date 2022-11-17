# -*- coding: utf-8 -*-
from telnetlib import EC
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {"platformName": "Android", "appium:deviceName": "aaa", "appium:appPackage": "com.osell.id",
                "appium:appActivity": ".main.OsellIdLaunchActivity", "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True, "appium:unicodeKeyboard": True}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        print("setup")
    def test_demo(self):
        print("test—demo-start")
        self.driver.implicitly_wait(10)
        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
        el6.send_keys("bag")
        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
        el7.click()
        el8 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
        el8.click()
        el9 = self.driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/ouka_products_collect")
        el9.click()
        print("test—demo-end")

    def test_capabilitis(self):
        # # 隐式等待
        print("test-demo-2-start")
        self.driver.implicitly_wait(10)
        #
        # # 死等
        # sleep(20)

        # 显示等待
        # WebDriverWait(等待的对象, 等待的时长,什么时候执行)  until的函数注释（翻译）：调用驱动程序提供的方法作为参数，直到返回值不是False。
        # # 方法一在WebDriverWait初始化时传入了driver参数，然后调用until方法，传入了一个lambda匿名函数
        # WebDriverWait(self.driver, 15).until(self.driver.find_element(by=AppiumBy.ID, value=""))

        # 方法二 locator的参数就是我们传入的loc，loc是什么呢，就是(By.ID,'#su')这种。
        # WebDriverWait(self.driver).until(EC.presence_of_element_located(loc))
        # WebDriverWait(self.driver).until(EC.presence_of_element_located(by=id()))
        # 写法1和写法2不同的是外层没有包含显示等待的类。
        #
        # 方法三
        # Expected Conditions的使用场景有2种
        # 直接在断言中使用
        # 与WebDriverWait配合使用，动态等待页面上元素出现或者消失
        # visibility_of_element_located: 判断某个元素是否可见.可见代表元素非隐藏，并且元素的宽和高都不等于0
        # WebDriverWait(self.driver).until(expected_conditions.visibility_of_element_located(By.ID, ''))


        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
        el6.send_keys("草莓")
        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
        el7.click()
        print("test-demo-2-end")


    def test_xpath(self):

        # 查找
        # //*[@text='登录]
        # //*[contains(@resource-id, 'login'")]
        # 条件匹配
        # //*[contains(@resource-id, 'login') and contains(@text, '登录")]]
        # //*[contains(@text,'登录')or contains(@label,'登录")]
        self.driver.find_element(AppiumBy.XPATH,value="//*[@text = '自选' and cantains(@resource-id,'tab_name')]").click()



    def teardown(self):
        print("treardown")
        # pass
        self.driver.quit()
