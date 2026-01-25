from pages.home_page import HomePage
from pages.product_page import ProductPage


class TestReview:

    def test_add_review_to_iphone(self):
        name = "Elinaelinaelina"
        review_text = "Nice phone thanks Nice phone thanks"

        home = HomePage().open()
        home.search("iPhone")
        home.open_iphone_from_results()

        product = ProductPage()
        product.rate_five_stars()
        product.fill_name(name)
        product.fill_review(review_text)
        product.submit_review()
        product.should_see_success_message()
