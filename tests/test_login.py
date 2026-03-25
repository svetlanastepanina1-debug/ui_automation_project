import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.login_page.login_page import LoginPage


@pytest.mark.ui
def test_login_user1_success(driver, env_data):
    login_url = env_data["urls"]["login"]
    driver.get(login_url)
    login_page = LoginPage(driver)

    login_page.login(env_data["users"]["user_1"]["login"], env_data["users"]["user_1"]["password"])

    WebDriverWait(driver, 15).until(lambda d: d.current_url != login_url)
    assert "login" not in driver.current_url.lower(), "Ожидалось успешное перенаправление после user1"


@pytest.mark.ui
def test_login_user2_fail(driver, env_data):
    login_url = env_data["urls"]["login"]
    driver.get(login_url)
    login_page = LoginPage(driver)

    login_page.login(env_data["users"]["user_2"]["login"], env_data["users"]["user_2"]["password"])

    WebDriverWait(driver, 15).until(lambda d: d.current_url == login_url)
    assert driver.current_url == login_url, "Ожидалось, что не удастся залогиниться user2"
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message"))
    )
    assert error_message.is_displayed(), "Ожидалось отображение сообщения об ошибке при неудачной попытке логина user2"
