from playwright.sync_api import Page, expect
from allureWraper import BasePage
import allure

class CheckOutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.deliverToThisAddressBtn = page.get_by_test_id("secondary-continue-button")
        self.paymentMethodText = page.locator("#checkout-paymentOptionPanel")

    # @allure.step("validating the visibility of deliver to the address")
    def validateTheVisibilityOfdeliverToThisAddressBtn(self):
        expect(self.deliverToThisAddressBtn).to_be_visible()

    
    # @allure.step("validating the visibility of payment method")
    def validateTheVisibilityOfpaymentMethodText(self):
        expect(self.paymentMethodText).to_be_visible()