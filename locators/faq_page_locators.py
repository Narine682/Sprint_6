from selenium.webdriver.common.by import By

class FAQPageLocators:
    FAQ_QUESTION_BUTTON = (By.CSS_SELECTOR, ".accordion__button")
    FAQ_ANSWER = (By.CSS_SELECTOR, ".accordion__panel")
