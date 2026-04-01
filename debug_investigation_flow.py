import os
import time
import random
import string
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ui.pages.login_page.login_page import LoginPage
from ui.pages.dashboard_page.dashboard_page import DashboardPage
from ui.pages.investigations_page import InvestigationsPage
from ui.pages.investigations_page.investigations_locators import InvestigationsLocators

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
    title = 'Test Investigation ' + ''.join(random.choice(string.ascii_letters) for _ in range(10))
    investigation_id = 'ID-' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    print('Creating title:', title)
    investigations.click_add_investigation()
    investigations.fill_investigation_title(title)
    investigations.fill_investigation_id(investigation_id)
    investigations.select_ship_facility()
    investigations.select_event_datetime()
    investigations.save_new_investigation()
    print('Saved, waiting for title')
    found = investigations.wait_for_investigation_with_title(title, timeout=30)
    print('wait_for_investigation_with_title returned', found)
    if found:
        print('FOUND new row!')
    else:
        # print current row texts
        rows = investigations.get_investigation_rows()
        print('Rows count after save:', len(rows))
        for i, row in enumerate(rows[:10], 1):
            print(i, repr(row.element.text))
finally:
    time.sleep(5)
    driver.quit()
