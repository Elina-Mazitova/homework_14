import allure
from selene import browser, be, have


class ComparisonPage:
    url = "/index.php?route=product/compare"

    @allure.step("Открыть страницу сравнения")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Выполнить поиск товара '{query}'")
    def search(self, query: str):
        browser.element('[name="search"]').set_value(query).press_enter()
        return self

    @allure.step("Добавить товар '{product_name}' в сравнение")
    def add_product_to_comparison(self, product_name: str):
        product = browser.element(
            f'//a[normalize-space()="{product_name}"]/ancestor::div[contains(@class,"product-layout")]'
        )
        compare_button = product.element('.btn-compare').should(be.visible)
        browser.driver.execute_script("arguments[0].click();", compare_button.locate())
        return self

    @allure.step("Добавить первый товар из результатов поиска в сравнение")
    def add_first_product_to_comparison(self):
        first_product = browser.element('(//div[contains(@class,"product-layout")])[1]')
        compare_button = first_product.element('.btn-compare')
        browser.driver.execute_script("arguments[0].click();", compare_button.locate())
        return self

    @allure.step("Проверить уведомление об успешном добавлении")
    def should_see_success_toast(self):
        browser.element('.toast').should(be.visible).should(have.text("Success: You have added"))
        return self

    @allure.step("Проверить, что товар '{product_name}' есть в списке сравнения")
    def should_contain_product(self, product_name: str):
        browser.element(f'//a[normalize-space()="{product_name}"]').should(be.visible)
        return self
