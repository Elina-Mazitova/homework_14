import allure
from pages.sorting_page import SortingPage


class TestSorting:

    @allure.title("Сортировка товаров по цене: от высокой к низкой")
    @allure.tag("sorting", "regression")
    def test_sort_by_price_high_to_low(self):
        sorting_page = SortingPage().open_category("33")

        sorting_page.sort_by("Price (High > Low)")
        prices = sorting_page.get_prices()

        with allure.step("Проверяем, что цены отсортированы по убыванию"):
            assert prices == sorted(prices, reverse=True), "Товары не отсортированы по убыванию цены"
