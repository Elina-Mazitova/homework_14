from selene import browser, be
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class TestSorting:
    def test_sort_by_price_high_to_low(self):
        BasePage().open("/index.php?route=product/category&path=33")

        sort_dropdown = browser.element('select[id^="input-sort"]').should(be.visible)

        select = Select(sort_dropdown.get_actual_webelement())
        select.select_by_visible_text("Price (High > Low)")

        prices = [
            el.get_actual_webelement().text
            for el in browser.all('.price-new')
        ]

        prices = [
            float(p.replace('$', '').replace(',', '').strip())
            for p in prices if '$' in p
        ]

        assert prices == sorted(prices, reverse=True), "Товары не отсортированы по убыванию цены"
