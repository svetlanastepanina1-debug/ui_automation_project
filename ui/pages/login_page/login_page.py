from ui.pages.login_page.base_element import BaseElement
from ui.pages.login_page.locators import LoginLocators


class LoginPage(BaseElement):
    """Page Object для страницы логина"""

    def __init__(self, driver):
        super().__init__(driver, None)

    def email_field(self):
        return BaseElement(self.driver, LoginLocators.EMAIL_INPUT)

    def password_field(self):
        return BaseElement(self.driver, LoginLocators.PASSWORD_INPUT)

    def login_button(self):
        return BaseElement(self.driver, LoginLocators.LOGIN_BUTTON)

    def set_email(self, email: str):
        self.email_field().send_keys(email)

    def set_password(self, password: str):
        self.password_field().send_keys(password)

    def click_login(self):
        self.login_button().click()

    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
