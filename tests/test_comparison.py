from selene import browser, be, have
import allure

from pages.base_page import BasePage


class TestComparison:
    @allure.step("Добавление первого товара в сравнение")
    def test_add_product_to_comparison(self):
        BasePage().open("/index.php?route=product/category&path=25")

        first_product = browser.all('.product-layout')[0]
        compare_button = first_product.element('.btn-compare').should(be.visible)

        browser.driver().execute_script("arguments[0].click();", compare_button.get_actual_webelement())

        browser.element('.toast').should(be.visible).should(have.text("Success: You have added"))
