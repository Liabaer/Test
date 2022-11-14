# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestDemo:
    def setup(self):
        caps = {"platformName": "Android", "appium:deviceName": "aaa", "appium:appPackage": "com.osell.id",
                "appium:appActivity": ".main.OsellIdLaunchActivity", "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True, "appium:unicodeKeyboard": True}

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_demo(self):
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

    def test_capabilitis(self):
        self.driver.implicitly_wait(10)
        el5 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
        el5.click()
        el6 = self.driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
        el6.send_keys("草莓")
        el7 = self.driver.find_element(by=AppiumBy.XPATH,
                                       value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
        el7.click()

    def teardown(self):
        # pass
        self.driver.quit()
