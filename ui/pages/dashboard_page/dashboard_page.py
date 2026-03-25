from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from ui.pages.login_page.base_element import BaseElement
from ui.pages.dashboard_page.locators import DashboardLocators


class AlertRow(BaseElement):
    """Элемент строки алерта в таблице"""

    def __init__(self, driver, row_element=None):
        super().__init__(driver, DashboardLocators.FIRST_ALERT_ROW)
        if row_element:
            self.element = row_element
        else:
            self.element = self.find()

    def get_screenshot_img(self):
        return self.element.find_element(By.XPATH, ".//td[1]//img")

    def get_description(self):
        return self.element.find_element(By.XPATH, ".//td[2]")

    def get_vessel(self):
        return self.element.find_element(By.XPATH, ".//td[3]")

    def get_location(self):
        return self.element.find_element(By.XPATH, ".//td[4]")

    def get_time(self):
        return self.element.find_element(By.XPATH, ".//td[5]")

    def get_duration(self):
        return self.element.find_element(By.XPATH, ".//td[6]")

    def get_status(self):
        return self.element.find_element(By.XPATH, ".//td[7]")

    def get_priority(self):
        return self.element.find_element(By.XPATH, ".//td[11]//span")

    def click(self):
        self.element.click()


class VideoPopup(BaseElement):
    """Элемент модального окна с видео"""

    def __init__(self, driver):
        super().__init__(driver, DashboardLocators.VIDEO_POPUP)

    def get_title(self):
        return BaseElement(self.driver, DashboardLocators.POPUP_TITLE)

    def get_close_button(self):
        return BaseElement(self.driver, DashboardLocators.POPUP_CLOSE_BUTTON)

    def get_video_tab(self):
        return BaseElement(self.driver, DashboardLocators.VIDEO_TAB)

    def get_photo_tab(self):
        return BaseElement(self.driver, DashboardLocators.PHOTO_TAB)

    def get_live_stream_tab(self):
        return BaseElement(self.driver, DashboardLocators.LIVE_STREAM_TAB)

    def get_video_element(self):
        return BaseElement(self.driver, DashboardLocators.POPUP_VIDEO)

    def get_download_button(self):
        return BaseElement(self.driver, DashboardLocators.DOWNLOAD_BUTTON)

    def get_weather_info(self):
        return BaseElement(self.driver, DashboardLocators.WEATHER_INFO_CONTAINER)

    def get_timeline_start_time(self):
        return BaseElement(self.driver, DashboardLocators.TIMELINE_START_TIME)

    def get_timeline_start_event(self):
        return BaseElement(self.driver, DashboardLocators.TIMELINE_START_EVENT)

    def get_timeline_end_time(self):
        return BaseElement(self.driver, DashboardLocators.TIMELINE_END_TIME)

    def get_timeline_end_event(self):
        return BaseElement(self.driver, DashboardLocators.TIMELINE_END_EVENT)

    def get_what_happened_input(self):
        return BaseElement(self.driver, DashboardLocators.WHAT_HAPPENED_INPUT)

    def get_prevent_input(self):
        return BaseElement(self.driver, DashboardLocators.PREVENT_INPUT)

    def get_steps_taken_input(self):
        return BaseElement(self.driver, DashboardLocators.STEPS_TAKEN_INPUT)

    def get_happened_before_value(self):
        return BaseElement(self.driver, DashboardLocators.HAPPENED_BEFORE_VALUE)

    def get_hurt_or_damaged_value(self):
        return BaseElement(self.driver, DashboardLocators.HURT_OR_DAMAGED_VALUE)

    def get_similar_incidents_value(self):
        return BaseElement(self.driver, DashboardLocators.SIMILAR_INCIDENTS_VALUE)

    def close_popup(self):
        self.get_close_button().click()

    def switch_to_video_tab(self):
        self.get_video_tab().click()

    def switch_to_photo_tab(self):
        self.get_photo_tab().click()

    def switch_to_live_stream_tab(self):
        self.get_live_stream_tab().click()

    def download_video(self):
        self.get_download_button().click()


class DashboardPage(BaseElement):
    """Page Object для страницы дашборда/оповещений"""

    URL = "https://test.evist.nl/dashboard"

    def __init__(self, driver):
        super().__init__(driver, None)

    def open(self):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        self.driver.get(self.URL)
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(DashboardLocators.FIRST_ALERT_ROW)
        )

    def get_first_alert_row(self):
        return AlertRow(self.driver)

    def get_alert_rows(self):
        rows = self.driver.find_elements(*DashboardLocators.ALERT_ROWS)
        return [AlertRow(self.driver, row) for row in rows]

    def get_video_popup(self):
        return VideoPopup(self.driver)

    def click_first_alert_row(self):
        first_row = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(DashboardLocators.FIRST_ALERT_ROW)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_row)
        first_row.click()

    def click_first_video_alert_row(self):
        try:
            self.click_first_alert_row()
            return True
        except Exception as ex:
            print(f"ERROR: click_first_video_alert_row failed: {type(ex).__name__}: {ex}")
            return False

    def wait_for_video_popup(self, timeout=30):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(DashboardLocators.VIDEO_POPUP)
        )

    def wait_for_video_popup_element(self, timeout=30):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(DashboardLocators.POPUP_VIDEO)
        )

    def is_video_popup_open(self):
        try:
            return self.video_popup().is_displayed()
        except Exception:
            return False

    def is_video_visible(self):
        try:
            return self.popup_video().is_displayed()
        except Exception:
            return False

    def get_video_src(self):
        return self.popup_video().find().get_attribute("src")
