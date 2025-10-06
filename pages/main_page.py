from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
class MainPage:
    locators = MainPageLocators
    @classmethod
    def open_main(cls, driver, url):
        driver.get(url)

    @classmethod
    def click_order_top(cls, driver):
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*cls.locators.ORDER_BUTTON_TOP))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(cls.locators.ORDER_BUTTON_TOP))
        driver.find_element(*cls.locators.ORDER_BUTTON_TOP).click()

    @classmethod
    def click_order_bottom(cls, driver):
        driver.execute_script("arguments[0].scrollLnoView(true);", driver.find_element(*cls.locators.ORDER_BUTTON_BOTTOM))
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(cls.locators.ORDER_BUTTON_TOP))
        driver.find_element(*cls.locators.ORDER_BUTTON_BOTTOM).click()

    @classmethod
    def click_scooter_logo(cls, driver):
        driver.find_element(*cls.locators.SCOOTER_LOGO).click()

    @classmethod
    def click_yandex_logo(cls, driver):
        driver.find_element(*cls.locators.YANDEX_LOGO).click()

    @classmethod
    def click_faq_question_button(cls, driver, index):
        buttons = BasePage.finds(driver, cls.locators.FAQ_QUESTION_BUTTON)
        driver.execute_script("arguments[0].scrollLnoView(true);",buttons[index])

    @classmethod
    def get_faq_answer_text(cls, driver, index):
        answers = BasePage.finds(driver, cls.locators.FAQ_ANSWER)
        return answers[index].text

    @classmethod
    def accept_cookies(cls, driver):
        possible_classes = ["App_CookieConsent__1yUIN", "App_CookieText__1sbqp"]
        for class_name in possible_classes:
            try:
                btn = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, class_name))
                )
                btn.click()
                break
            except:
                continue

