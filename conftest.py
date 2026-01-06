import pytest
from playwright.sync_api import sync_playwright
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.resultsPage import ResultsPage
from pages.shoppingCartPage import ShoppingCart
from pages.checkOutPage import CheckOutPage


from utils.readingJson import readJsonData
credentials  = "testData/credentials.json"
testData = readJsonData(credentials)
import os


@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(slow_mo=3000)
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

@pytest.fixture()
def results_page(page):
    results_page = ResultsPage(page)
    return results_page

@pytest.fixture()
def shoppingCart_page(page):
    shoppingCart_page = ShoppingCart(page)
    return shoppingCart_page

@pytest.fixture()
def CheckOut_page(page):
    CheckOut_page = CheckOutPage(page)
    return CheckOut_page

@pytest.fixture(scope="function")
def logInUsingvalidcreds(page, home_Page, login_page):
    home_Page.launchTheAmazonBrowser()
    home_Page.hoverOnAccountsBtn()
    # home_Page.clickOnSignInBtn()
    login_page.enterEmailID("trainingplaywright@gmail.com")
    login_page.clickOnContinueBtn()
    login_page.enterPassword("Welcome@04")
    login_page.clickOnContinueBtn()
    yield


import pytest
import allure

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()

#     if report.when == "call" and report.failed:
#         page = item.funcargs.get("page", None)
#         if page:
#             screenshot = page.screenshot()
#             allure.attach(
#                 screenshot,
#                 name="Failure Screenshot",
#                 attachment_type=allure.attachment_type.PNG
#             )
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots for setup, call, and teardown failures
    if report.failed:
        page = item.funcargs.get("page", None)
        if page:
            step = report.when  # setup / call / teardown
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Failure Screenshot ({step})",
                attachment_type=allure.attachment_type.PNG
            )

