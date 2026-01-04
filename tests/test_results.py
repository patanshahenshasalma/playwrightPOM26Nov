from playwright.sync_api import Page, expect
import pytest

def test_verifySearchResults(page: Page, home_Page, results_page, logInUsingvalidcreds):
    home_Page.launchTheAmazonBrowser()
    home_Page.searchForTheProduct("iphone")
    resultsText = []
    errors =[]
    for i in range(results_page.resultsText.count()):
        # print(results_page.resultsText.nth(i).get_attribute("aria-label"))
        resultsText.append(results_page.resultsText.nth(i).text_content())

    print(resultsText[0])
    for text in resultsText:
        try:
            assert "iphone" in text.lower() or "apple" in text.lower()
        except Exception as e:
            errors.append(e)

    assert errors.count==0, "displayed results has results other than iphone and apple"

def test_validate_addToCartFunctionality(page:Page, home_Page, results_page, logInUsingvalidcreds):
    home_Page.launchTheAmazonBrowser()
    home_Page.searchForTheProduct("iphone")
    results_page.clickOnAddToCartBtn("iPhone 15")
    results_page.validateTheVisibilityOfDecementIconAfterAddingTheElementToCart()
    results_page.clickOnDecrementicon()




