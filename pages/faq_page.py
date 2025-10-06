from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPageLocators

class FAQPage:
    locators = MainPageLocators
    @classmethod
    def open_question(cls, driver, index):
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(cls.locators.FAQ_QUESTION_BUTTON)
        )
        button = buttons[index]
        driver.execute_script("arguments[0].scrollIntoView(true);",button)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(button))
        button.click()

    @classmethod
    def get_answer(cls, driver, index):
         answers = WebDriverWait(driver, 10).until(
             EC.presence_of_all_elements_located(cls.locators.FAQ_ANSWER)
         )
         return answers[index].text