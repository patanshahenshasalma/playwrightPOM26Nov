from playwright.sync_api import Page, expect
from utils.commonMethods import CommonMethods


class HomePage():
    def __init__(self, page: Page):
        self.page = page
        self.accntBtn = page.locator("#nav-link-accountList")
        self.signInBtn = page.locator(".nav-action-inner")
        ##
        self.searchTab = page.locator("input#twotabsearchtextbox")
        self.searchBtn = page.locator("input#nav-search-submit-button")

    def hoverOnAccountsBtn(self):
        self.accntBtn.hover()

    def clickOnSignInBtn(self):
        expect(self.signInBtn).to_be_visible()
        self.signInBtn.click()
        # commonMethods = CommonMethods()
        # commonMethods.clickOnAnelement(self.signInBtn)

    def launchTheAmazonBrowser(self):
        self.page.goto("https://www.amazon.in/")
        self.accntBtn.wait_for(timeout=40000)

    def searchForTheProduct(self, value):
        self.searchTab.fill(value)
        self.searchBtn.click()

        