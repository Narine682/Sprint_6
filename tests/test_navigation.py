import pytest
import allure
from pages.main_page import MainPage
from data import BASE_URL

@allure.feature("Navigation")
class TestNavigation:
    @allure.title("Логотип Самоката возвращает на главную страницу")
    def test_scooter_logo_navigates_home(self, driver):
        main = MainPage(driver)
        main.open_main(BASE_URL)
        main.click_order_bottom()
        main.click_scooter_logo()
        current_url = main.current_url()
        assert "qa-scooter.praktikum-services.ru" in current_url,  "Не открылся главный сайт"

    @allure.title("Клик по лдготипу Яндекса открывает новое окно")
    def test_yandex_logo_opens_new_tab(self, driver):
        main = MainPage(driver)
        main.open_main(BASE_URL)
        main.click_yandex_logo()
        handles = main.get_window_handles()
        assert len(handles) >= 2, "Не отклылось новое окно при клике на логотип Яндекса"

    @allure.title("Новое окно после клика по логотипу Яндекса открывает Dzen")
    def test_yandex_logo_opens_dzen_site(self, driver):
        main = MainPage(driver)
        main.open_main(BASE_URL)
        main.click_yandex_logo()
        handles = main.get_window_handles()
        main.switch_to_window(handles[-1])
        current_url = main.current_url()
        assert "dzen.ru" in current_url or "zen.yandex" in current_url, "Не открылся сайт Dzen"