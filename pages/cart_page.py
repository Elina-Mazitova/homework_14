import allure
from selene import browser, be, have


class CartPage:
    url = "/index.php?route=checkout/cart"

    @allure.step("Очистить корзину")
    def clear(self):
        browser.open(self.url)
        remove_buttons = browser.all('button[data-original-title="Remove"]')
        for btn in remove_buttons:
            btn.click()
        return self

    @allure.step("Добавить Nikon D300 из результатов поиска в корзину")
    def add_nikon_from_search_results(self):
        product_image = browser.element('//img[@alt="Nikon D300"]')

        product_image.hover()

        add_button = browser.element(
            '//img[@alt="Nikon D300"]'
            '/ancestor::div[contains(@class,"product-thumb-top")]'
            '//div[contains(@class,"product-action")]'
            '//button[contains(@class,"btn-cart")]'
        ).should(be.visible)

        browser.driver.execute_script("arguments[0].click();", add_button.locate())
        return self

    @allure.step("Проверить, что отобразился тост об успешном добавлении")
    def should_show_success_icon(self):
        browser.element('.toast').should(be.visible).should(have.text("Success"))
        return self

    @allure.step("Открыть корзину")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Проверить, что товар '{product_name}' есть в корзине")
    def should_contain_product(self, product_name):
        browser.element(
            '#content table tbody tr td:nth-child(2) a'
        ).should(have.text(product_name))
        return self


