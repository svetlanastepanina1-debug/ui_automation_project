import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.login_page.login_page import LoginPage


LOGIN_URL = "https://test.evist.nl/login/"


@pytest.mark.ui
def test_login_user1_success(driver, env_data):
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)

    login_page.login(env_data["users"]["user_1"]["login"], env_data["users"]["user_1"]["password"])

    WebDriverWait(driver, 15).until(lambda d: d.current_url != LOGIN_URL)
    assert "login" not in driver.current_url.lower(), "Ожидалось успешное перенаправление после user1"


@pytest.mark.ui
def test_login_user2_fail(driver, env_data):
    driver.get(LOGIN_URL)
    login_page = LoginPage(driver)

    login_page.login(env_data["users"]["user_2"]["login"], env_data["users"]["user_2"]["password"])

    WebDriverWait(driver, 15).until(lambda d: d.current_url == LOGIN_URL)
    assert driver.current_url == LOGIN_URL, "Ожидалось, что не удастся залогиниться user2"

    # При наличии сообщения об ошибке можно добавить дополнительную проверку:
    # error = WebDriverWait(driver, 5).until(
    #     EC.visibility_of_element_located((By.XPATH, "//div[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'invalid') or contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'wrong')]"))
    # )
    # assert error is not None
