# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 设置selenium的chrome驱动
driver = webdriver.Chrome(executable_path="/Users/Tu/Downloads/chromedriver")

# 使用test前缀可以让pytest执行
def test_selenium():
    driver.get("https://www.baidu.com")
    # 找到input框html的name选择器的值，此处的wd是百度搜索框的name的值
    elem = driver.find_element(By.NAME, "wd")
    # 向input框输入搜索内容
    elem.send_keys("python")
    # 模拟按下回车
    elem.send_keys(Keys.RETURN)
    # 所以selenium就是操作html的元素，模拟输入、点击等功能。
