import allure
from selene import browser, by, be, have
from pages.base_page import BasePage
from pages.category_page import CategoryPage

class HomePage(BasePage):
    relative_url = "/"

    @allure.step("Открыть главную страницу")
    def open_home(self):
        return self.open(self.relative_url)

    @allure.step("Выполнить поиск по запросу: {query}")
    def search(self, query: str):
        browser.element('[name="search"]').type(query).press_enter()

    @allure.step("Проверить, что результаты содержат {text}")
    def should_see_result(self, text: str):
        products = browser.all('.product-thumb')
        products.should(have.size_at_least(1))
        products.first.should(have.text(text))

    @allure.step("Открыть меню Shop by Category")
    def open_shop_by_category(self):
        button = browser.element('//a[@aria-label="Shop by Category"]').locate()
        browser.driver.execute_script("arguments[0].click();", button)
        return self

    @allure.step("Выбрать категорию {category} в Shop by Category")
    def select_category(self, category: str) -> CategoryPage:
        browser.element(f'//a[normalize-space()="{category}"]').should(be.clickable).click()
        return CategoryPage()
