import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilis import allure_attachments


@pytest.fixture(autouse=True)
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1280,800")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.set_driver(driver)

    yield
    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == 'call' and result.failed:
        attach.attach_screenshot()
        allure_attachments.attach_page_source()
        allure_attachments.attach_logs()
