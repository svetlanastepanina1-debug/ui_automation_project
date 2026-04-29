"""Локальные фикстуры и хуки только для каталога tests/."""

import allure
import pytest


@pytest.fixture(scope="function")
def investigations_page(login):
    from ui.pages.dashboard_page.dashboard_page import DashboardPage
    from ui.pages.investigations_page.investigations_page import InvestigationsPage

    with allure.step("Открыть дашборд после входа"):
        dashboard = DashboardPage(login)
        dashboard.open()
    with allure.step("Перейти в раздел Investigations через меню"):
        investigations = InvestigationsPage(login)
        investigations.click_investigations_menu()
    return investigations
