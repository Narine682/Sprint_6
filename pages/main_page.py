from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from locators.common_locators import CommonLocators


class MainPage(BasePage):
    locators = MainPageLocators

    def open_main(self, url):
        self.open(url)


    def click_order_top(self):
        element = self.find(self.locators.ORDER_BUTTON_TOP)
        self.scroll_into_view(element)
        self.click(self.locators.ORDER_BUTTON_TOP)


    def click_order_bottom(self):
        element = self.find(self.locators.ORDER_BUTTON_BOTTOM)
        self.scroll_into_view(element)
        self.click(self.locators.ORDER_BUTTON_BOTTOM)


    def click_scooter_logo(self):
        self.click(CommonLocators.LOGO_SCOOTER)


    def click_yandex_logo(self):
        self.click((CommonLocators.LOGO_YANDEX))


    def click_faq_question_button(self, index):
        buttons = self.find(self.locators.FAQ_QUESTION_BUTTON)
        button = buttons[index]
        self.scroll_into_view(button)
        button.click()


    def get_faq_answer_text(self, index):
        answers = self.finds(self.locators.FAQ_ANSWER)
        return answers[index].text



    def accept_cookies(self):
        possible_classes = ["App_CookieConsent__1yUIN", "App_CookieText__1sbqp"]
        for class_name in possible_classes:
            try:
                btn = self.wait. until(
                    EC.element_to_be_clickable((By.CLASS_NAME, class_name))
                )
                btn.click()
                break
            except:
                continue

