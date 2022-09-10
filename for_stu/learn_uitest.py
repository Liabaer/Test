# -*- coding: utf-8 -*-
from selenium import webdriver



driver = webdriver.Chrome(executable_path="/Users/Tu/Downloads/chromedriver")    # Chrome浏览器


# 打开网页
driver.get("https://www.baidu.com")