from playwright.sync_api import Page, expect
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils.readingJson import readJsonData
import json
import os
credentials  = "testData\\multipleCreds.json"
testData = readJsonData(credentials)


@pytest.mark.parametrize("username,password", [("training1playwright@gmail.com","Welcome@02")])
def test_logInUsingvalidcreds(page: Page, home_Page, login_page, username, password):
    home_Page.launchTheAmazonBrowser()
    home_Page.hoverOnAccountsBtn()
    home_Page.clickOnSignInBtn()
    login_page.enterEmailID(username)
    login_page.clickOnContinueBtn()
    login_page.enterPassword(password)
    login_page.clickOnContinueBtn()










