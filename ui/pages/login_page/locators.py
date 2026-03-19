from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@name="loginEmail"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@name="loginPassword"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and normalize-space(text())="Log in"]')
