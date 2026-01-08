import allure
from selene import browser, have, be

class CartPage:
    relative_url = "/"

    @allure.step("Открыть главную страницу")
    def open(self):
        browser.open_url("https://ecommerce-playground.lambdatest.io/")
        return self

    @allure.step("Добавить первый товар в корзину (JS‑клик)")
    def add_product(self):
        button = browser.driver().find_element("xpath", '//button[contains(@title,"Add to Cart")]')
        browser.driver().execute_script("arguments[0].click();", button)

    @allure.step("Проверить, что отобразилась иконка успешного добавления в корзину")
    def should_show_success_icon(self):
        # ждём появления toast-уведомления
        browser.element('.toast').should(be.visible).should(have.text("Success"))
