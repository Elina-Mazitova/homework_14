import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()
    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "128.0")
    options.set_capability("selenoid:options", {
        "enableVNC": True,
        "enableVideo": True
    })
    # включаем логи браузера
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

    remote_url = os.getenv("REMOTE_URL", "https://user1:1234@selenoid.autotests.cloud/wd/hub")

    driver = webdriver.Remote(
        command_executor=remote_url,
        options=options
    )

    # 📌 Настраиваем глобальный selene.browser
    browser.config.driver = driver
    browser.config.base_url = os.getenv("BASE_URL", "https://ecommerce-playground.lambdatest.io")
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    # 📌 Артефакты всегда
    try:
        allure.attach(driver.get_screenshot_as_png(),
                      name="screenshot",
                      attachment_type=AttachmentType.PNG)
        allure.attach(driver.page_source,
                      name="page_source",
                      attachment_type=AttachmentType.HTML)
    except Exception:
        pass

    try:
        logs = driver.get_log("browser")
        text = "\n".join([f"{l['level']}: {l['message']}" for l in logs])
        allure.attach(text, "browser_logs", AttachmentType.TEXT, ".log")
    except Exception:
        pass

    video_url = f"https://selenoid.autotests.cloud/video/{driver.session_id}.mp4"
    allure.attach(
        f"<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video></body></html>",
        name="video",
        attachment_type=AttachmentType.HTML
    )

    driver.quit()
