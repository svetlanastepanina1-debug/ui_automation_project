import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ui.pages.investigation_page.investigations_page import InvestigationsPage


@pytest.mark.ui
def test_open_investigations_page(login):
    investigations = InvestigationsPage(login)
    investigations.open()

    first_row = investigations.get_first_investigation_row()
    assert first_row is not None, "Ожидалось, что на странице Investigations есть хотя бы одна строка"

    assert first_row.get_description().text, "Описание расследования не должно быть пустым"
    assert first_row.get_vessel().text, "Название судна не должно быть пустым"
    assert first_row.get_incident().text, "Текст инцидента не должен быть пустым"
    assert first_row.get_team().text, "Команда не должна быть пустой"
    assert first_row.get_timestamp().text, "Время расследования не должно быть пустым"

    first_row.click()
    assert investigations.is_initial_info_tab_opened(), "Ожидалось, что вкладка Initial info откроется после клика по строке"


@pytest.mark.ui
def test_investigations_menu_link_navigates(login):
    investigations = InvestigationsPage(login)
    investigations.click_investigations_menu()

    WebDriverWait(login, 20).until(EC.url_contains("/investigations"))
    assert investigations.is_opened(), "Ожидалось, что переход по ссылке Investigations откроет страницу /investigations"


@pytest.mark.ui
def test_investigation_row_is_clickable(login):
    investigations = InvestigationsPage(login)
    investigations.open()

    first_row = investigations.get_first_investigation_row()
    assert first_row is not None, "Ожидалось, что первая строка расследования доступна"
    assert first_row.get_status_icon().is_displayed(), "Иконка статуса в строке расследования должна быть видна"
    first_row.click()
