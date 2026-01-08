import allure
from pages.home_page import HomePage

class TestSearch:
    def test_search_product(self):
        home = HomePage().open_home()
        home.search("iPhone")
        home.should_see_result("iPhone")