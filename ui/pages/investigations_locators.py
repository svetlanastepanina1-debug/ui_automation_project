from selenium.webdriver.common.by import By


class InvestigationsLocators:
    INVESTIGATIONS_MENU_LINK = (
        By.XPATH,
        "//a[contains(@href, '/investigations') and normalize-space()='Investigations']",
    )
    INVESTIGATION_ROW = (By.XPATH, "//tr[contains(@class, 'GG0CbPqv')]")
    ROW_STATUS_ICON = (By.XPATH, ".//td[1]")
    ROW_DESCRIPTION = (By.XPATH, ".//td[2]")
    ROW_VESSEL = (By.XPATH, ".//td[3]")
    ROW_INCIDENT = (By.XPATH, ".//td[4]")
    ROW_TEAM = (By.XPATH, ".//td[5]")
    ROW_TIMESTAMP = (By.XPATH, ".//td[6]")
    INITIAL_INFO_TAB = (
        By.XPATH,
        "//div[@data-state='selected' and contains(@class, 'tab-active')]//span[normalize-space()='Initial info']",
    )
