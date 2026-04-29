import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.dashboard_page.dashboard_page import DashboardPage


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_open_dashboard(login):
    """Тест открытия страницы дашборда"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд"):
        dashboard.open()

    with allure.step("Проверить наличие строк алертов"):
        alert_rows = dashboard.get_alert_rows()
        assert len(alert_rows) > 0, "Ожидалось наличие алертов на дашборде"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_click_first_alert(login):
    """Тест клика по первой строке алерта"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд"):
        dashboard.open()

    with allure.step("Кликнуть по первой строке с видео-алертом"):
        result = dashboard.click_first_video_alert_row()
        assert result, "Не удалось кликнуть по первой строке алерта"

    with allure.step("Проверить появление popup с видео"):
        popup = dashboard.get_video_popup()
        WebDriverWait(login, 10).until(EC.visibility_of_element_located(popup.locator))
        assert popup.is_displayed(), "Popup с видео не появился"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@allure.story("Video popup")
@pytest.mark.skip(reason="временно не работает, требует доработки")
@pytest.mark.ui
def test_video_popup_elements(login):
    """Тест элементов в popup видео"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд и popup"):
        dashboard.open()
        dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    with allure.step("Проверить заголовок и видео"):
        title_element = popup.get_title()
        assert title_element.is_displayed(), "Заголовок popup не отображается"
        video_element = popup.get_video_element()
        assert video_element.is_displayed(), "Видео элемент не отображается"

    with allure.step("Проверить вкладки и кнопку скачивания"):
        video_tab = popup.get_video_tab()
        assert video_tab.is_displayed(), "Вкладка Video не отображается"
        download_button = popup.get_download_button()
        assert download_button.find() is not None, "Кнопка скачивания не найдена"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_alert_row_data(login):
    """Тест данных в строке алерта"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд"):
        dashboard.open()

    with allure.step("Проверить поля первой строки алерта"):
        first_alert = dashboard.get_first_alert_row()
        description = first_alert.get_description().text
        assert description, "Описание алерта отсутствует"
        vessel = first_alert.get_vessel().text
        assert vessel, "Название судна отсутствует"
        location = first_alert.get_location().text
        assert location, "Локация отсутствует"
        time = first_alert.get_time().text
        assert time, "Время алерта отсутствует"
        status = first_alert.get_status().text
        assert status, "Статус алерта отсутствует"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_popup_weather_info(login):
    """Тест погодной информации в popup"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд и popup"):
        dashboard.open()
        dashboard.click_first_video_alert_row()

    with allure.step("Проверить блок погоды"):
        popup = dashboard.get_video_popup()
        weather_info = popup.get_weather_info()
        assert weather_info.is_displayed(), "Погодная информация не отображается"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_popup_input_fields(login):
    """Тест полей ввода в popup"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд и popup"):
        dashboard.open()
        dashboard.click_first_video_alert_row()

    with allure.step("Проверить поля ввода"):
        popup = dashboard.get_video_popup()
        what_happened = popup.get_what_happened_input()
        assert what_happened.find() is not None, "Поле 'What happened' не найдено"
        prevent_input = popup.get_prevent_input()
        assert prevent_input.find() is not None, "Поле 'How can we prevent this?' не найдено"
        steps_taken = popup.get_steps_taken_input()
        assert steps_taken.find() is not None, "Поле 'Steps taken after the incident' не найдено"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_popup_additional_fields(login):
    """Тест дополнительных полей в popup"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд и popup"):
        dashboard.open()
        dashboard.click_first_video_alert_row()

    with allure.step("Проверить дополнительные поля"):
        popup = dashboard.get_video_popup()
        happened_before = popup.get_happened_before_value()
        assert happened_before.find() is not None, "Поле 'Happened before' не найдено"
        hurt_or_damaged = popup.get_hurt_or_damaged_value()
        assert hurt_or_damaged.find() is not None, "Поле 'Hurt or damaged' не найдено"
        similar_incidents = popup.get_similar_incidents_value()
        assert similar_incidents.find() is not None, "Поле 'Similar incidents' не найдено"


@allure.epic("EVist UI")
@allure.feature("Dashboard")
@pytest.mark.ui
def test_close_popup(login):
    """Тест закрытия popup"""
    dashboard = DashboardPage(login)

    with allure.step("Открыть дашборд и popup"):
        dashboard.open()
        dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()
    with allure.step("Проверить, что popup отображается"):
        assert popup.is_displayed(), "Popup не появился"

    with allure.step("Закрыть popup и проверить исчезновение"):
        popup.close_popup()
        WebDriverWait(login, 10).until(EC.invisibility_of_element_located(popup.locator))
        assert not dashboard.is_video_popup_open(), "Popup не закрылся"
