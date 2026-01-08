from pages.home_page import HomePage

def test_open_mice_and_trackballs():
    home = HomePage().open_home()
    home.open_shop_by_category()
    category = home.select_category("Mice and Trackballs")
    category.should_have_header("Mice and Trackballs")
