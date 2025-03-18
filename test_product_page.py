from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    title = page.get_title()
    price = page.get_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price_title(title, price)


# запускаем тест pytest -s -v --tb=line --language=en test_product_page.py