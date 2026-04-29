import random
import string

import allure
import pytest

from ui.pages.investigations_page import InvestigationsPage


def _random_eng_text(length: int = 12) -> str:
    return "Test Investigation " + "".join(random.choice(string.ascii_letters) for _ in range(length))


@allure.epic("EVist UI")
@allure.feature("Investigations")
@allure.story("Создание расследования")
@pytest.mark.ui
def test_create_new_investigation(investigations_page):
    investigations = investigations_page
    title = _random_eng_text(10)
    investigation_id = "ID-" + "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))

    with allure.step("Заполнить форму нового расследования"):
        investigations.click_add_investigation()
        investigations.fill_investigation_title(title)
        investigations.fill_investigation_id(investigation_id)
        investigations.select_ship_facility()
        investigations.select_event_datetime()
        investigations.save_new_investigation()

    with allure.step("Проверить открытие вкладки Initial info"):
        assert investigations.wait_for_initial_info_tab(), (
            "Ожидалось, что после сохранения откроется вкладка Initial info"
        )

    with allure.step("Вернуться к списку и проверить появление записи"):
        investigations.click_investigations_list_link()
        assert investigations.wait_for_investigation_with_title(title), (
            f"Ожидалось, что расследование '{title}' появится в списке Investigations"
        )
