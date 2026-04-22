import allure

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
        with allure.step("Ввести email в поле логина"):
            self.email_field().send_keys(email)

    def set_password(self, password: str):
        with allure.step("Ввести пароль"):
            self.password_field().send_keys(password)

    def click_login(self):
        with allure.step("Нажать кнопку входа"):
            self.login_button().click()

    def login(self, email: str, password: str):
        with allure.step("Заполнить форму входа и отправить"):
            self.set_email(email)
            self.set_password(password)
            self.click_login()
