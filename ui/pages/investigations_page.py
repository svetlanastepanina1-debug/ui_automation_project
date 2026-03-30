from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ui.pages.investigations_locators import InvestigationsLocators
from ui.pages.login_page.base_element import BaseElement


class InvestigationRow(BaseElement):
    """Строка расследования в таблице Investigations."""

    def __init__(self, driver, row_element=None):
        super().__init__(driver, InvestigationsLocators.INVESTIGATION_ROW)
        self.element = row_element if row_element is not None else self.find()

    def get_status_icon(self):
        return self.element.find_element(*InvestigationsLocators.ROW_STATUS_ICON)

    def get_description(self):
        return self.element.find_element(*InvestigationsLocators.ROW_DESCRIPTION)

    def get_vessel(self):
        return self.element.find_element(*InvestigationsLocators.ROW_VESSEL)

    def get_incident(self):
        return self.element.find_element(*InvestigationsLocators.ROW_INCIDENT)

    def get_team(self):
        return self.element.find_element(*InvestigationsLocators.ROW_TEAM)

    def get_timestamp(self):
        return self.element.find_element(*InvestigationsLocators.ROW_TIMESTAMP)

    def click(self):
        self.element.click()


class InvestigationsPage(BaseElement):
    """Page Object для страницы Investigations."""

    URL = "https://test.evist.nl/investigations"

    def __init__(self, driver):
        super().__init__(driver, None)

    def open(self):
        self.driver.get(self.URL)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(InvestigationsLocators.INVESTIGATION_ROW)
        )

    def get_investigations_menu_link(self):
        return BaseElement(self.driver, InvestigationsLocators.INVESTIGATIONS_MENU_LINK)

    def click_investigations_menu(self):
        link = self.get_investigations_menu_link()
        link.click()
        WebDriverWait(self.driver, 20).until(EC.url_contains("/investigations"))

    def get_investigation_rows(self):
        rows = self.driver.find_elements(*InvestigationsLocators.INVESTIGATION_ROW)
        return [InvestigationRow(self.driver, row) for row in rows]

    def get_first_investigation_row(self):
        rows = self.get_investigation_rows()
        return rows[0] if rows else None

    def click_first_investigation_row(self):
        first_row = self.get_first_investigation_row()
        if first_row is None:
            raise ValueError("Нет ни одной строки расследования для клика")
        first_row.click()
        return first_row

    def get_initial_info_tab(self):
        return BaseElement(self.driver, InvestigationsLocators.INITIAL_INFO_TAB)

    def is_initial_info_tab_opened(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(InvestigationsLocators.INITIAL_INFO_TAB)
            )
            return True
        except TimeoutException:
            return False

    def is_opened(self):
        return "/investigations" in self.driver.current_url.lower()
