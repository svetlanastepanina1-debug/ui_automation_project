import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait

from ui.pages.login_page.login_page import LoginPage


@allure.epic("EVist UI")
@allure.feature("Авторизация")
@pytest.mark.ui
def test_login_user1_success(driver, env_data):
    login_url = env_data["urls"]["login"]
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу входа"):
        driver.get(login_url)

    with allure.step("Выполнить вход под user_1"):
        login_page.login(env_data["users"]["user_1"]["login"], env_data["users"]["user_1"]["password"])

    with allure.step("Проверить успешный редирект после входа"):
        WebDriverWait(driver, 15).until(lambda d: d.current_url != login_url)
        assert "login" not in driver.current_url.lower(), "Ожидалось успешное перенаправление после user1"


@allure.epic("EVist UI")
@allure.feature("Авторизация")
@pytest.mark.ui
def test_login_user2_fail(driver, env_data):
    login_url = env_data["urls"]["login"]
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу входа"):
        driver.get(login_url)

    with allure.step("Попытка входа под user_2 (ожидается отказ)"):
        login_page.login(env_data["users"]["user_2"]["login"], env_data["users"]["user_2"]["password"])

    with allure.step("Проверить, что пользователь остался на странице логина"):
        WebDriverWait(driver, 15).until(lambda d: d.current_url == login_url)
        assert driver.current_url == login_url, "Ожидалось, что не удастся залогиниться user2"
