import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import HomePage
from pages.loginPage import LoginPage


from utils.readingJson import readJsonData
credentials  = "testData/credentials.json"
testData = readJsonData(credentials)
import os


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=3000)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def home_Page(page):
    home_Page = HomePage(page)
    return home_Page

@pytest.fixture()
def login_page(page):
    login_page = LoginPage(page)
    return login_page

