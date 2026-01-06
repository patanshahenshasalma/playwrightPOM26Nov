from playwright.sync_api import Page, expect
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils.readingJson import readJsonData
import json
import os
credentials  = "testData/multipleCreds.json"
testData = readJsonData(credentials)


# @pytest.mark.parametrize("username,password", [("trainingplaywright@gmail.com","Welcome@02")])
# @pytest.mark.dependency(name="login")
# @pytest.mark.order(0)
# @pytest.mark.smoke()
# def test_logInUsingvalidcreds(page: Page, home_Page, login_page, username, password):
#     home_Page.launchTheAmazonBrowser()
#     home_Page.hoverOnAccountsBtn()
#     home_Page.clickOnSignInBtn()
#     login_page.enterEmailID(username)
#     login_page.clickOnContinueBtn()
#     login_page.enterPassword(password)
#     login_page.clickOnContinueBtn()

@pytest.mark.order(1)
@pytest.mark.smoke()
@pytest.mark.productCheckout()
def test_validateTheVisibilityofSwitchAccount(page:Page, home_Page, logInUsingvalidcreds ):
    home_Page.hoverOnAccountsBtn()
    home_Page.validateTheVisibilityOfSwitchAccount()
    

# HTML

# pip install pytest-html








