import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
import os
from dotenv import load_dotenv
from utils.script_os import TMP_DIR



load_dotenv()
selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

print(f"SELENOID_URL = {selenoid_url}")
print(f"SELENOID_LOGIN = {selenoid_login}")
print(f"SELENOID_PASS = {selenoid_pass}")



@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version', default='127.0')

    options = Options()

    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)

    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.base_url = 'https://webmaster.leads.su'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver = driver

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
