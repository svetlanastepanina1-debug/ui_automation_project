from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException


class BaseElement:
    """Обертка над WebElement для базовых действий."""

    def __init__(self, driver: WebDriver, locator: tuple, timeout: int = 10):
        self.driver = driver
        self.locator = locator
        self.timeout = timeout

    def find(self) -> WebElement:
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located(self.locator)
            )
            return element
        except TimeoutException:
            # Fallback to regular find if wait fails
            return self.driver.find_element(*self.locator)

    def click(self):
        element = self.find()
        element.click()
        return element

    def send_keys(self, value: str):
        element = self.find()
        element.clear()
        element.send_keys(value)
        return element

    def text(self) -> str:
        return self.find().text

    def is_displayed(self) -> bool:
        try:
            return self.find().is_displayed()
        except (NoSuchElementException, StaleElementReferenceException):
            return False
