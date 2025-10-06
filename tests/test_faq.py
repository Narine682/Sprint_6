import pytest
import allure
from pages.faq_page import FAQPage
from pages.main_page import MainPage
from data import BASE_URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@allure.feature("FAQ")
class TestFAQPage:

    @pytest.mark.parametrize("index", range(8))
    @allure.title("Проверка открытия ответа на вопрос {index}")
    def test_faq_question_opens(self, driver, index):
        MainPage.open_main(driver, BASE_URL)
        MainPage.accept_cookies(driver)
        FAQPage.open_question(driver, index)
        answer = FAQPage.get_answer(driver, index)
        assert answer and len(answer) > 0, f"Ответ для вопроса{index} пустой"

        @staticmethod
        def _accert_cookies(driver):
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