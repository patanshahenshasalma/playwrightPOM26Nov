from playwright.sync_api import Page, expect
from allureWraper import BasePage

class CheckOutPage():
    def __init__(self, page: Page):
        self.page = page
        self.deliverToThisAddressBtn = page.get_by_test_id("secondary-continue-button")
        self.paymentMethodText = page.locator("#checkout-paymentOptionPanel")


    def validateTheVisibilityOfdeliverToThisAddressBtn(self):
        expect(self.deliverToThisAddressBtn).to_be_visible()

    def validateTheVisibilityOfpaymentMethodText(self):
        expect(self.paymentMethodText).to_be_visible()