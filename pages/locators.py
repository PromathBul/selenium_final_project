from selenium.webdriver.common.by import By
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'div.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'div.register_form')

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_AFTER_ADD = (By.CSS_SELECTOR, '.alertinner p strong')
    TITLE_AFTER_ADD = (By.CSS_SELECTOR, '.alert-success:first-child strong')