
import pytest 

from pages.vertical import vertical

@pytest.mark.smoke
def test_trading_options_click(page):
    vertical_page = vertical(page)
    vertical_page.trading_options_click()

# def test_retail_and_ecommerce_options_click(page):
#     vertical_page = vertical(page)
#     vertical_page.retail_and_ecommerce_options_click()