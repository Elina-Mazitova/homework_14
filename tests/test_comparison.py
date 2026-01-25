import allure
from selene import browser

from pages.comparison import ComparisonPage


class TestComparison:

    @allure.title("Добавление товара Canon EOS 5D в список сравнения через поиск")
    @allure.tag("comparison", "smoke")
    def test_add_canon_to_comparison_from_search(self):
        product_name = "Canon EOS 5D"

        comparison_page = ComparisonPage()

        # 1. Открываем главную страницу
        browser.open("/")

        # 2. Выполняем поиск
        comparison_page.search(product_name)

        # 3. Добавляем товар в сравнение
        comparison_page.add_product_to_comparison(product_name)
        comparison_page.should_see_success_toast()

        # 4. Открываем страницу сравнения
        comparison_page.open()
        comparison_page.should_contain_product(product_name)
