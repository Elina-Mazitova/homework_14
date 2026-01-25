import allure
from selene import browser, be, have


class ProductPage:

    @allure.step("Открыть страницу товара по product_id={product_id}")
    def open(self, product_id: int):
        browser.open(f"/index.php?route=product/product&product_id={product_id}")
        return self

    @allure.step("Поставить 5 звезд")
    def rate_five_stars(self):
        browser.element(
            '#form-review .select-rating span label:nth-child(2)'
        ).should(be.visible).click()
        return self

    @allure.step("Заполнить имя")
    def fill_name(self, name: str):
        browser.element('#input-name').set_value(name)
        return self

    @allure.step("Заполнить текст отзыва")
    def fill_review(self, text: str):
        browser.element('#input-review').set_value(text)
        return self

    @allure.step("Отправить отзыв")
    def submit_review(self):
        browser.element('#button-review').click()
        return self

    @allure.step("Проверить успешное сообщение")
    def should_see_success_message(self):
        browser.element(
            '#form-review .alert.alert-success.alert-dismissible'
        ).should(be.visible)
        return self
