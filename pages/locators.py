from selenium.webdriver.common.by import By
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, 'div.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, 'div.register_form')

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')