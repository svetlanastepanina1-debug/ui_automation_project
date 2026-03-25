from selenium.webdriver.common.by import By


class DashboardLocators:
    # Alert rows
    FIRST_ALERT_ROW = (By.XPATH, "(//tr[contains(@class, 'GG0CbPqv')])[1]")
    ALERT_ROWS = (By.XPATH, "//tr[contains(@class, 'GG0CbPqv')]")

    # Alert row elements (relative to row)
    ALERT_SCREENSHOT_IMG = (By.XPATH, ".//td[1]//img")
    ALERT_DESCRIPTION = (By.XPATH, ".//td[2]")
    ALERT_VESSEL = (By.XPATH, ".//td[3]")
    ALERT_LOCATION = (By.XPATH, ".//td[4]")
    ALERT_TIME = (By.XPATH, ".//td[5]")
    ALERT_DURATION = (By.XPATH, ".//td[6]")
    ALERT_STATUS = (By.XPATH, ".//td[7]")
    ALERT_PRIORITY = (By.XPATH, ".//td[11]//span")

    # Video popup
    VIDEO_POPUP = (By.XPATH, "//div[contains(@class,'alert-modal') or contains(@class,'popup') or contains(@class,'modal')]")
    POPUP_VIDEO = (By.XPATH, "(//div[contains(@class,'alert-modal') or contains(@class,'popup') or contains(@class,'modal')]//video) | //video")

    # Popup header
    POPUP_TITLE = (By.XPATH, "//div[contains(@class,'popup')]//h2[contains(@class,'popup-title')]")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class,'popup')]//button[contains(@class,'popup-close')]")

    # Tabs
    VIDEO_TAB = (By.XPATH, "//div[contains(@class,'tab') and contains(@class,'tab-active')]//span[text()='Video']")
    PHOTO_TAB = (By.XPATH, "//div[contains(@class,'tab')]//span[text()='Photo']")
    LIVE_STREAM_TAB = (By.XPATH, "//div[contains(@class,'tab')]//span[text()='Live stream']")

    # Video controls
    DOWNLOAD_BUTTON = (By.XPATH, "//button[contains(@class,'download-button')]")

    # Weather info
    WEATHER_INFO_CONTAINER = (By.XPATH, "//div[contains(@class,'weather-info')]")
    WEATHER_CLOUDY = (By.XPATH, "//div[contains(@class,'weather-info')]//svg[contains(@class,'weather-cloudy')]")
    WEATHER_CURRENT = (By.XPATH, "//div[contains(@class,'weather-info')]//svg[contains(@class,'weather-arrow-up')][1]")
    WEATHER_WIND = (By.XPATH, "//div[contains(@class,'weather-info')]//svg[contains(@class,'weather-arrow-up')][2]")
    WEATHER_WAVES = (By.XPATH, "//div[contains(@class,'weather-info')]//svg[contains(@class,'weather-waves')]")

    # Timeline
    TIMELINE_CONTAINER = (By.XPATH, "//div[contains(@class,'grid') and contains(@class,'grid-cols-[6rem_24px_1fr]')]")
    TIMELINE_START_TIME = (By.XPATH, "(//div[contains(@class,'grid') and contains(@class,'grid-cols-[6rem_24px_1fr]')]//div[@class='text-right pr-1 text-text-secondary whitespace-nowrap'])[1]")
    TIMELINE_START_EVENT = (By.XPATH, "(//div[contains(@class,'grid') and contains(@class,'grid-cols-[6rem_24px_1fr]')]//div[@class='pl-1 text-text-primary break-words'])[1]")
    TIMELINE_END_TIME = (By.XPATH, "(//div[contains(@class,'grid') and contains(@class,'grid-cols-[6rem_24px_1fr]')]//div[@class='text-right pr-1 text-text-secondary whitespace-nowrap'])[2]")
    TIMELINE_END_EVENT = (By.XPATH, "(//div[contains(@class,'grid') and contains(@class,'grid-cols-[6rem_24px_1fr]')]//div[@class='pl-1 text-text-primary break-words'])[2]")

    # Input fields
    WHAT_HAPPENED_LABEL = (By.XPATH, "//div[@class='input-label' and text()='What happened']")
    WHAT_HAPPENED_INPUT = (By.XPATH, "//div[@class='input-label' and text()='What happened']/following-sibling::div[@class='input-content']")
    PREVENT_INPUT_LABEL = (By.XPATH, "//div[@class='input-label' and text()='How can we prevent this?']")
    PREVENT_INPUT = (By.XPATH, "//div[@class='input-label' and text()='How can we prevent this?']/following-sibling::div[@class='input-content']")
    STEPS_TAKEN_LABEL = (By.XPATH, "//div[@class='input-label' and text()='Steps taken after the incident']")
    STEPS_TAKEN_INPUT = (By.XPATH, "//div[@class='input-label' and text()='Steps taken after the incident']/following-sibling::div[@class='text-xs text-text-primary font-normal leading-tight']")

    # Additional fields
    HAPPENED_BEFORE_LABEL = (By.XPATH, "//div[@class='input-label' and text()='Happened before']")
    HAPPENED_BEFORE_VALUE = (By.XPATH, "//div[@class='input-label' and text()='Happened before']/following-sibling::div[@class='input-content']")
    HURT_OR_DAMAGED_LABEL = (By.XPATH, "//div[@class='input-label' and text()='Hurt or damaged']")
    HURT_OR_DAMAGED_VALUE = (By.XPATH, "//div[@class='input-label' and text()='Hurt or damaged']/following-sibling::div[@class='input-content']")
    SIMILAR_INCIDENTS_LABEL = (By.XPATH, "//div[@class='input-label' and text()='Similar incidents']")
    SIMILAR_INCIDENTS_VALUE = (By.XPATH, "//div[@class='input-label' and text()='Similar incidents']/following-sibling::div[@class='input-content']")
