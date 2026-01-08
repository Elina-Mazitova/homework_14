import allure
from selene import browser, be, have
from pages.base_page import BasePage


class ComparisonPage(BasePage):

    @allure.step("Открываем страницу категории с path={path}")
    def open_category(self, path: str):
        self.open(f"/index.php?route=product/category&path={path}")
        return self

    @allure.step("Добавляем первый товар в сравнение")
    def add_first_product_to_comparison(self):
        first_product = browser.all('.product-layout')[0]
        compare_button = first_product.element('.btn-compare').should(be.visible)
        browser.driver().execute_script(
            "arguments[0].click();", compare_button.get_actual_webelement()
        )
        return self

    @allure.step("Проверяем уведомление об успешном добавлении")
    def should_see_success_toast(self):
        browser.element('.toast').should(be.visible).should(have.text("Success: You have added"))
        return self
