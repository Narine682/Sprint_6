import pytest
import allure
from pages.faq_page import FAQPage
from pages.main_page import MainPage
from data import BASE_URL



@allure.feature("FAQ")
class TestFAQPage:

    @pytest.mark.parametrize("index", range(8))
    @allure.title("Проверка открытия ответа на вопрос {index}")
    def test_faq_question_opens(self, driver, index):
        main = MainPage(driver)
        faq = FAQPage(driver)
        main.open_main(BASE_URL)
        main.accept_cookies()
        faq.open_question(index)
        answer = faq.get_answer(index)
        assert answer and len(answer) > 0, f"Ответ для вопроса{index} пустой"

