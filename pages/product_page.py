from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_button_basket()
        self.save_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def check_price_title(self, title, price):
        price_after_add = self.get_price_after_add()
        title_after_add = self.get_title_after_add()
        print(title_after_add)
        assert self.comparision_values(price, price_after_add) and \
            self.comparision_values(title, title_after_add), \
            'Price or title is showed incorrect'

    def should_be_button_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            'Button for adding product to basket is not presented'

    def get_title(self):
        return self.save_element(*ProductPageLocators.TITLE).text

    def get_price(self):
        return self.save_element(*ProductPageLocators.PRICE).text

    def get_price_after_add(self):
        return self.save_element(*ProductPageLocators.PRICE_AFTER_ADD).text

    def get_title_after_add(self):
        return self.save_element(*ProductPageLocators.TITLE_AFTER_ADD).text


