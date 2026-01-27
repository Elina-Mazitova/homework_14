from pages.home_page import HomePage


class TestCart:
    def test_add_product_to_cart(self, cart_cleaner):
        product_name = "Nikon D300"

        home = HomePage().open()
        home.search(product_name)

        cart_cleaner.add_nikon_from_search_results()
        cart_cleaner.should_show_success_icon()

        cart_cleaner.open()
        cart_cleaner.should_contain_product(product_name)