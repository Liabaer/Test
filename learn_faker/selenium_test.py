# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope='module')
def browser():
    # 启动Chrome浏览器并打开Web应用程序
    driver = webdriver.Chrome()
    driver.get('http://localhost:5000')
    yield driver

    # 关闭浏览器
    driver.quit()

def test_data_displayed(browser):
    # 检查测试数据是否正确显示在Web页面上
    assert browser.find_element(By.XPATH, '//td[text()="张三"]')

