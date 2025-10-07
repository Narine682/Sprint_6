from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.faq_page_locators import FAQPageLocators
from pages.base_page import BasePage

class FAQPage(BasePage):
    locators = FAQPageLocators

    def open_question(self, index):
        buttons = self.wait.until(
            EC.presence_of_all_elements_located(self.locators.FAQ_QUESTION_BUTTON)
        )
        button = buttons[index]
        self.scroll_into_view(button)
        self.wait.until(EC.element_to_be_clickable(button))
        button.click()


    def get_answer(self, index):
        answers = self.wait.until(
             EC.presence_of_all_elements_located(self.locators.FAQ_ANSWER)
        )
        return answers[index].text