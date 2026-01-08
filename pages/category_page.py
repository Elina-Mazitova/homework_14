import allure
from selene import browser, have

class CategoryPage:
    @allure.step("Проверить, что заголовок страницы содержит {category}")
    def should_have_header(self, category: str):
        browser.element('h1.h4').should(have.text(category))
        browser.all('.product-thumb').should(have.size_at_least(1))
