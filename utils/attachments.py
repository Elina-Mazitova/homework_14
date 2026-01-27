import os
import allure
from allure_commons.types import AttachmentType


def attach_screenshot(driver):
    try:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )
    except Exception as e:
        allure.attach(str(e), "screenshot_error", AttachmentType.TEXT)


def attach_page_source(driver):
    try:
        allure.attach(
            driver.page_source,
            name="page_source",
            attachment_type=AttachmentType.HTML
        )
    except Exception as e:
        allure.attach(str(e), "page_source_error", AttachmentType.TEXT)

def add_logs(browser):
        log = "".join(f'{text}\n' for text in browser.driver.execute("getLog", {'type': 'browser'})['value'])
        allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')

def attach_video(driver):
    session_id = driver.session_id
    video_host = os.getenv("SELENOID_VIDEO_HOST", "selenoid.autotests.cloud")

    video_url = f"https://{video_host}/video/{session_id}.mp4"

    allure.attach(
        f"<html><body><video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'></video></body></html>",
        name="video",
        attachment_type=AttachmentType.HTML
    )
