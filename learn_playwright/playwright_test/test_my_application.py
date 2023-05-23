# -*- coding: utf-8 -*-
import re
from playwright.sync_api import Page, expect


def test_homepage_has_Playwright_in_title_and_get_started_link_linking_to_the_intro_page(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.标题包含字符串"Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator 创建一个定位器
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.期望与属性值完全相等
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.点击开始链接
    get_started.click()

    # Expects the URL to contain intro.要求url包含介绍
    expect(page).to_have_url(re.compile(".*intro"))

