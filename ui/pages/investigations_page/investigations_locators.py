from selenium.webdriver.common.by import By


class InvestigationsLocators:
    INVESTIGATIONS_MENU_LINK = (
        By.XPATH,
        "//a[@href='/investigations' and normalize-space()='Investigations']",
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
    INVESTIGATIONS_LIST_LINK = (
        By.XPATH,
        "//a[@href='/investigations' and normalize-space()='Investigations']",
    )

    ADD_INVESTIGATION_BUTTON = (
        By.XPATH,
        "//button[.//*[local-name()='use' and contains(@*[local-name()='href'], '#plus')] and @type='button']",
    )
    CREATE_DIALOG = (
        By.XPATH,
        "//div[@role='dialog' and contains(@class,'popup') and .//span[contains(normalize-space(), 'Report an Accident')]]",
    )
    CREATE_DIALOG_TITLE_INPUT = (
        By.XPATH,
        "//div[@role='dialog']//input[@id='name']",
    )
    CREATE_DIALOG_SHIP_SELECT_BUTTON = (
        By.XPATH,
        "//div[@role='dialog']//button[@type='button' and @aria-haspopup='menu']",
    )
    CREATE_DIALOG_SHIP_OPTION = (
        By.XPATH,
        "//div[contains(@data-state,'open')]//div[@role='menuitem'][1]",
    )
    CREATE_DIALOG_DATETIME_BUTTON = (
        By.XPATH,
        "//div[@role='dialog']//button[@type='button' and contains(@aria-haspopup,'dialog') and .//span[contains(normalize-space(),'Select date and time')]]",
    )
    CREATE_DIALOG_DATETIME_TODAY_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'datetime-action') and normalize-space()='Today']",
    )
    CREATE_DIALOG_DATETIME_OK_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'datetime-action') and contains(@class,'datetime-action--primary') and normalize-space()='Ok']",
    )
    CREATE_DIALOG_ID_INPUT = (
        By.XPATH,
        "//div[@role='dialog']//input[@id='number']",
    )
    CREATE_DIALOG_SAVE_BUTTON = (
        By.XPATH,
        "//div[@role='dialog']//button[@type='submit' and contains(@class,'btn-orange')]",
    )
