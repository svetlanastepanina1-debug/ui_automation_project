import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ui.pages.investigations_page import InvestigationsPage


@allure.epic("EVist UI")
@allure.feature("Investigations")
@pytest.mark.ui
def test_open_investigations_page(login):
    investigations = InvestigationsPage(login)

    with allure.step("Открыть страницу Investigations"):
        investigations.open()

    with allure.step("Проверить первую строку таблицы и поля данных"):
        first_row = investigations.get_first_investigation_row()
        assert first_row is not None, "Ожидалось, что на странице Investigations есть хотя бы одна строка"

        assert first_row.get_description().text, "Описание расследования не должно быть пустым"
        assert first_row.get_vessel().text, "Название судна не должно быть пустым"
        assert first_row.get_incident().text, "Текст инцидента не должен быть пустым"
        assert first_row.get_team().text, "Команда не должна быть пустой"
        assert first_row.get_timestamp().text, "Время расследования не должно быть пустым"

    with allure.step("Клик по строке и проверка вкладки Initial info"):
        first_row.click()
        assert investigations.is_initial_info_tab_opened(), (
            "Ожидалось, что вкладка Initial info откроется после клика по строке"
        )


@allure.epic("EVist UI")
@allure.feature("Investigations")
@pytest.mark.ui
def test_investigations_menu_link_navigates(login):
    investigations = InvestigationsPage(login)

    with allure.step("Перейти в раздел через меню"):
        investigations.click_investigations_menu()

    with allure.step("Проверить URL и открытие страницы"):
        WebDriverWait(login, 20).until(EC.url_contains("/investigations"))
        assert investigations.is_opened(), "Ожидалось, что переход по ссылке Investigations откроет страницу /investigations"


@allure.epic("EVist UI")
@allure.feature("Investigations")
@pytest.mark.ui
def test_investigation_row_is_clickable(login):
    investigations = InvestigationsPage(login)

    with allure.step("Открыть страницу Investigations"):
        investigations.open()

    with allure.step("Проверить кликабельность первой строки"):
        first_row = investigations.get_first_investigation_row()
        assert first_row is not None, "Ожидалось, что первая строка расследования доступна"
        assert first_row.get_status_icon().is_displayed(), "Иконка статуса в строке расследования должна быть видна"
        first_row.click()
