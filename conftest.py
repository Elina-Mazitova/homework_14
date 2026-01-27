import os
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.remote_connection import RemoteConnection, ClientConfig

from pages.cart_page import CartPage
from utils.attachments import (
    attach_screenshot,
    attach_page_source,
    add_logs,
    attach_video
)

load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    selenoid_url = os.getenv("SELENOID_URL")

    # ==== Браузер и версия из .env ====
    browser_name = os.getenv("BROWSER_NAME", "chrome")
    browser_version = os.getenv("BROWSER_VERSION", "128.0")

    options = Options()
    options.set_capability("browserName", browser_name)

    if selenoid_url:
        options.set_capability("browserVersion", browser_version)

    # ==== Логи браузера ====
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    if selenoid_url:
        options.set_capability("selenoid:options", {
            "enableVNC": True,
            "enableVideo": True
        })

        selenoid_user = os.getenv("SELENOID_USER")
        selenoid_password = os.getenv("SELENOID_PASSWORD")
        selenoid_host = os.getenv("SELENOID_HOST", "selenoid.autotests.cloud")

        # ClientConfig вместо user:pass@url
        client_config = ClientConfig(
            remote_server_addr=f"https://{selenoid_host}",
            username=selenoid_user,
            password=selenoid_password
        )

        remote_connection = RemoteConnection(
            None,
            client_config=client_config
        )

        driver = webdriver.Remote(
            command_executor=remote_connection,
            options=options
        )

    else:
        driver = webdriver.Chrome()

    # ==== Selene ====
    browser.config.driver = driver
    browser.config.base_url = os.getenv(
        "BASE_URL",
        "https://ecommerce-playground.lambdatest.io"
    )
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    # ==== Аттачи ====
    attach_screenshot(driver)
    attach_page_source(driver)
    add_logs(browser)

    if selenoid_url:
        attach_video(driver)

    driver.quit()


@pytest.fixture
def cart_cleaner():
    cart = CartPage()
    cart.clear()
    return cart
