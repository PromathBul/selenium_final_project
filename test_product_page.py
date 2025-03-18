from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('path', [*range(6), pytest.param('7', marks=pytest.mark.xfail), *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, path):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{path}'
    page = ProductPage(browser, link)
    page.open()
    title = page.get_title()
    price = page.get_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_price_title(title, price)


# запускаем тест pytest -s -v --tb=line --language=en test_product_page.py