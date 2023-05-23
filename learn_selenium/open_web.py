# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://mycitra-dev.ey.net/login')
