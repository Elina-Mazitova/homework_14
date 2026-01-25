from pages.cart_page import CartPage
from pages.home_page import HomePage


class TestCart:
    def test_add_product_to_cart(self):
        product_name = "Nikon D300"

        home = HomePage().open()
        home.search(product_name)

        cart = CartPage()

        cart.clear()

        home.search(product_name)

        cart.add_nikon_from_search_results()
        cart.should_show_success_icon()

        cart.open()
        cart.should_contain_product(product_name)
