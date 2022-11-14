# # This sample code uses the Appium python client v2
# # pip install Appium-Python-Client
# # Then you can paste this into a file and simply run with Python
#
# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
#
# # For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
#
# caps = {}
# caps["platformName"] = "android"
# caps["appium:deviceName"] = "aaa"
# caps["appium:appPackage"] = "com.osell.id"
# caps["appium:appActivity"] = ".main.OsellIdLaunchActivity"
# caps["appium:ensureWebviewsHavePages"] = True
# caps["appium:nativeWebScreenshot"] = True
# caps["appium:newCommandTimeout"] = 3600
# caps["appium:connectHardwareKeyboard"] = True
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
#
# el1 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
# el1.click()
# el2 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
# el2.click()
# el4 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
# el4.send_keys("草莓")
# el5 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/constraint_label")
# el5.click()
# el6 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
# el6.click()
# el6.send_keys("包")
#
# driver.quit()


# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:deviceName"] = "aaa"
caps["appium:appPackage"] = "com.osell.id"
caps["appium:appActivity"] = ".main.OsellIdLaunchActivity"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

# 隐式等待 避免因为页面还没加载出来，找不到元素的报错
driver.implicitly_wait(10)
el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")
el5.click()
el6 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/et_search")
el6.send_keys("bag")
el7 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]")
el7.click()
el8 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.GridView/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
el8.click()
el9 = driver.find_element(by=AppiumBy.ID, value="com.osell.id:id/ouka_products_collect")
el9.click()

driver.quit()