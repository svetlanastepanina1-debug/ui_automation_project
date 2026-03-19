from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    """Обертка над WebElement для базовых действий."""

    def __init__(self, driver: WebDriver, locator: tuple):
        self.driver = driver
        self.locator = locator

    def find(self) -> WebElement:
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
        return self.find().is_displayed()
