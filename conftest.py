import os

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_configure(config):
    config.addinivalue_line("markers", "ui: mark test as a UI test")


@pytest.fixture(scope="session")
def env_data():
    env_path = os.path.join(os.path.dirname(__file__), "env.data.yml")
    with open(env_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver, env_data):
    LOGIN_URL = "https://test.evist.nl/login/"
    driver.get(LOGIN_URL)
    from ui.pages.login_page.login_page import LoginPage
    from selenium.webdriver.support.ui import WebDriverWait

    login_page = LoginPage(driver)
    login_page.login(env_data["users"]["user_1"]["login"], env_data["users"]["user_1"]["password"])

    WebDriverWait(driver, 20).until(lambda d: d.current_url and "login" not in d.current_url.lower())
    return driver
