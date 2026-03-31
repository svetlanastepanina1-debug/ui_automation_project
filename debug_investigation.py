import os
import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ui.pages.login_page.login_page import LoginPage
from ui.pages.dashboard_page.dashboard_page import DashboardPage
from ui.pages.investigations_page import InvestigationsPage
from ui.pages.investigations_locators import InvestigationsLocators

with open('env.data.yml', 'r', encoding='utf-8') as f:
    env = yaml.safe_load(f)

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-notifications')
options.add_argument('--disable-save-password-bubble')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-features=PasswordManagerOnboarding,NotificationTriggers,MediaRouter')
options.set_capability('unhandledPromptBehavior', 'accept')

driver = webdriver.Chrome(options=options)
try:
    driver.get(env['urls']['login'])
    login_page = LoginPage(driver)
    login_page.login(env['users']['user_1']['login'], env['users']['user_1']['password'])
    WebDriverWait(driver, 30).until(lambda d: d.current_url and 'login' not in d.current_url.lower())
    dashboard = DashboardPage(driver)
    dashboard.open()
    investigations = InvestigationsPage(driver)
    investigations.click_investigations_menu()
    print('Opened investigations page')
    investigations.click_add_investigation()
    time.sleep(2)
    print('Dialog found:', driver.find_element(*InvestigationsLocators.CREATE_DIALOG).is_displayed())
    print('Title input html:', driver.find_element(*InvestigationsLocators.CREATE_DIALOG_TITLE_INPUT).get_attribute('outerHTML'))
    print('Ship select html:', driver.find_element(*InvestigationsLocators.CREATE_DIALOG_SHIP_SELECT_BUTTON).get_attribute('outerHTML'))
    print('Datetime button html:', driver.find_element(*InvestigationsLocators.CREATE_DIALOG_DATETIME_BUTTON).get_attribute('outerHTML'))
    # Open ship menu
    driver.find_element(*InvestigationsLocators.CREATE_DIALOG_SHIP_SELECT_BUTTON).click()
    time.sleep(2)
    options_list = driver.find_elements(By.XPATH, "//div[contains(@data-state,'open')]//div[@role='menuitem']")
    print('Ship options count:', len(options_list))
    for idx, item in enumerate(options_list[:5], start=1):
        print(idx, 'text=', repr(item.text), 'html=', item.get_attribute('outerHTML')[:200])
    # Inspect save button state
    save_btn = driver.find_element(*InvestigationsLocators.CREATE_DIALOG_SAVE_BUTTON)
    print('Save button disabled attr:', save_btn.get_attribute('disabled'))
    print('Save button enabled state:', save_btn.is_enabled())
    # and all rows currently visible
    rows = driver.find_elements(*InvestigationsLocators.INVESTIGATION_ROW)
    print('Rows count before create:', len(rows))
    for i, row in enumerate(rows[:5], 1):
        print('row', i, repr(row.text))
finally:
    time.sleep(5)
    driver.quit()
