from pages.cart_page import CartPage

class TestCart:
    def test_add_product_shows_success_icon(self):
        cart = CartPage().open()
        cart.add_product()
        cart.should_show_success_icon()
