import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(autouse=True)
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.set_driver(driver)

    yield
    browser.quit()