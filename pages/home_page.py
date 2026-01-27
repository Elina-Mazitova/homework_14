import allure
from selene import browser, be, have


class HomePage:
    url = "/"

    @allure.step("Открыть главную страницу")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Выполнить поиск по запросу: {query}")
    def search(self, query: str):
        browser.element('[name="search"]').type(query).press_enter()
        return self

    @allure.step("Проверить, что результаты содержат {text}")
    def should_see_result(self, text: str):
        products = browser.all('.product-thumb')
        products.should(have.size_greater_than_or_equal(1))
        products.first.should(have.text(text))

    @allure.step("Открыть iPhone из результатов поиска")
    def open_iphone_from_results(self):
        browser.element('img[alt="iPhone"]').should(be.visible).click()
        return self