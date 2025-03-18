from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_button_basket()
        self.save_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()


    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), 'Button for adding product to basket is not presented'
