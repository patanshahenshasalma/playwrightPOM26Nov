from playwright.sync_api import Page, expect
import pytest
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils.readingJson import readJsonData
import json
credentials  = "testData/multipleCreds.json"
testData = readJsonData(credentials)

# parametrize(variable , assigning)
@pytest.mark.parametrize("username,password", [(testData["validCredential1"]["username"], testData["validCredential1"]["password"]), 
                                               (testData["inValidCredential2"]["username"], testData["inValidCredential2"]["password"] ), 
                                               (testData["inValidCredential1"]["username"], testData["inValidCredential1"]["password"])])
def test_logInUsingvalidcreds(page: Page, home_Page, login_page, username, password):
    home_Page.launchTheAmazonBrowser()
    home_Page.hoverOnAccountsBtn()
    home_Page.clickOnSignInBtn()
    # print(username)  
    login_page.enterEmailID(username)
    # login_page.enterEmailID(username)
    login_page.clickOnContinueBtn()
    login_page.enterPassword(password)
    # login_page.enterPassword(password)
    login_page.clickOnContinueBtn()










