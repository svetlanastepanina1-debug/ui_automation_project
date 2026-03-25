import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.dashboard_page.dashboard_page import DashboardPage


@pytest.mark.ui
def test_open_dashboard(login):
    """Тест открытия страницы дашборда"""
    dashboard = DashboardPage(login)
    dashboard.open()

    # Проверяем, что страница загрузилась и есть хотя бы одна строка алерта
    alert_rows = dashboard.get_alert_rows()
    assert len(alert_rows) > 0, "Ожидалось наличие алертов на дашборде"


@pytest.mark.ui
def test_click_first_alert(login):
    """Тест клика по первой строке алерта"""
    dashboard = DashboardPage(login)
    dashboard.open()

    # Кликаем по первой строке
    result = dashboard.click_first_video_alert_row()
    assert result, "Не удалось кликнуть по первой строке алерта"

    # Проверяем, что popup появился
    popup = dashboard.get_video_popup()
    WebDriverWait(login, 10).until(
        EC.visibility_of_element_located(popup.locator)
    )
    assert popup.is_displayed(), "Popup с видео не появился"


@pytest.mark.ui
def test_video_popup_elements(login):
    """Тест элементов в popup видео"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    # Проверяем заголовок
    title_element = popup.get_title()
    assert title_element.is_displayed(), "Заголовок popup не отображается"

    # Проверяем видео элемент
    video_element = popup.get_video_element()
    assert video_element.is_displayed(), "Видео элемент не отображается"

    # Проверяем вкладки
    video_tab = popup.get_video_tab()
    assert video_tab.is_displayed(), "Вкладка Video не отображается"

    # Проверяем кнопку скачивания
    download_button = popup.get_download_button()
    assert download_button.is_displayed(), "Кнопка скачивания не отображается"


@pytest.mark.ui
def test_alert_row_data(login):
    """Тест данных в строке алерта"""
    dashboard = DashboardPage(login)
    dashboard.open()

    first_alert = dashboard.get_first_alert_row()

    # Проверяем основные поля
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


@pytest.mark.ui
def test_popup_weather_info(login):
    """Тест погодной информации в popup"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    # Проверяем контейнер погодной информации
    weather_info = popup.get_weather_info()
    assert weather_info.is_displayed(), "Погодная информация не отображается"


@pytest.mark.ui
def test_popup_timeline(login):
    """Тест таймлайна в popup"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    # Проверяем элементы таймлайна
    start_time = popup.get_timeline_start_time()
    assert start_time.is_displayed(), "Время начала не отображается"

    start_event = popup.get_timeline_start_event()
    assert start_event.is_displayed(), "Событие начала не отображается"

    end_time = popup.get_timeline_end_time()
    assert end_time.is_displayed(), "Время окончания не отображается"

    end_event = popup.get_timeline_end_event()
    assert end_event.is_displayed(), "Событие окончания не отображается"


@pytest.mark.ui
def test_popup_input_fields(login):
    """Тест полей ввода в popup"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    # Проверяем поля ввода
    what_happened = popup.get_what_happened_input()
    assert what_happened.is_displayed(), "Поле 'What happened' не отображается"

    prevent_input = popup.get_prevent_input()
    assert prevent_input.is_displayed(), "Поле 'How can we prevent this?' не отображается"

    steps_taken = popup.get_steps_taken_input()
    assert steps_taken.is_displayed(), "Поле 'Steps taken after the incident' не отображается"


@pytest.mark.ui
def test_popup_additional_fields(login):
    """Тест дополнительных полей в popup"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()

    # Проверяем дополнительные поля
    happened_before = popup.get_happened_before_value()
    assert happened_before.is_displayed(), "Поле 'Happened before' не отображается"

    hurt_or_damaged = popup.get_hurt_or_damaged_value()
    assert hurt_or_damaged.is_displayed(), "Поле 'Hurt or damaged' не отображается"

    similar_incidents = popup.get_similar_incidents_value()
    assert similar_incidents.is_displayed(), "Поле 'Similar incidents' не отображается"


@pytest.mark.ui
def test_close_popup(login):
    """Тест закрытия popup"""
    dashboard = DashboardPage(login)
    dashboard.open()
    dashboard.click_first_video_alert_row()

    popup = dashboard.get_video_popup()
    assert popup.is_displayed(), "Popup не появился"

    # Закрываем popup
    popup.close_popup()

    # Проверяем, что popup исчез
    WebDriverWait(login, 10).until(
        EC.invisibility_of_element_located(popup.locator)
    )
    assert not popup.is_displayed(), "Popup не закрылся"
