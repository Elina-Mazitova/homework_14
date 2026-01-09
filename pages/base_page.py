from selene import browser

class BasePage:
    base_url = "https://ecommerce-playground.lambdatest.io"

    def open(self, relative_url=""):
        browser.open(self.base_url + relative_url)
        return self