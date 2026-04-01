import os

import pytest
import yaml
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def pytest_configure(config):
    config.addinivalue_line("markers", "ui: mark test as a UI test")


def _accept_unexpected_alert(driver, timeout=2):
    try:
        WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
    except TimeoutException:
        return None


@pytest.fixture(scope="session")
def env_data():
    if os.environ.get("BASE_URL"):
        return {
            "urls": {
                "base": os.environ["BASE_URL"],
                "login": os.environ["LOGIN_URL"],
                "dashboard": os.environ["DASHBOARD_URL"],
                "investigations": os.environ["INVESTIGATIONS_URL"],
            },
            "users": {
                "user_1": {
                    "login": os.environ["USER1_LOGIN"],
                    "password": os.environ["USER1_PASSWORD"],
                },
            },
        }

    env_path = os.path.join(os.path.dirname(__file__), "env.data.yml")
    with open(env_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-features=PasswordManagerOnboarding,NotificationTriggers,MediaRouter")

    if os.environ.get("HEADLESS", "").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "autofill.credit_card_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 2,
            "profile.default_content_setting_values.media_stream_mic": 2,
            "profile.default_content_setting_values.media_stream_camera": 2,
        },
    )
    options.set_capability("unhandledPromptBehavior", "accept")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login(driver, env_data):
    login_url = env_data["urls"]["login"]
    driver.get(login_url)
    from ui.pages.login_page.login_page import LoginPage

    login_page = LoginPage(driver)
    login_page.login(env_data["users"]["user_1"]["login"], env_data["users"]["user_1"]["password"])

    _accept_unexpected_alert(driver)

    WebDriverWait(driver, 20).until(lambda d: d.current_url and "login" not in d.current_url.lower())
    _accept_unexpected_alert(driver)
    return driver

@pytest.fixture(scope="function")
def investigations_page(login):
    from ui.pages.dashboard_page.dashboard_page import DashboardPage
    from ui.pages.investigations_page.investigations_page import InvestigationsPage

    dashboard = DashboardPage(login)
    dashboard.open()
    investigations = InvestigationsPage(login)
    investigations.click_investigations_menu()
    return investigations