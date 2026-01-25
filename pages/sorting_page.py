import allure
from selene import browser, be
from selenium.webdriver.support.ui import Select


class SortingPage:

    @allure.step("Открываем страницу категории с path={path}")
    def open_category(self, path: str):
        browser.open(f"/index.php?route=product/category&path={path}")
        return self

    @allure.step("Выбираем сортировку: {option_text}")
    def sort_by(self, option_text: str):
        sort_dropdown = browser.element('select[id^="input-sort"]').should(be.visible)
        select = Select(sort_dropdown.locate())
        select.select_by_visible_text(option_text)
        return self

    @allure.step("Собираем список цен товаров")
    def get_prices(self):
        prices = [
            el.locate().text
            for el in browser.all('.price-new')
        ]
        prices = [
            float(p.replace('$', '').replace(',', '').strip())
            for p in prices if '$' in p
        ]
        return prices
