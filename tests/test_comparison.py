import allure
from pages.comparison import ComparisonPage


class TestComparison:

    @allure.title("Добавление товара в список сравнения")
    @allure.tag("comparison", "smoke")
    def test_add_product_to_comparison(self):
        comparison_page = ComparisonPage().open_category("25")
        comparison_page.add_first_product_to_comparison()
        comparison_page.should_see_success_toast()