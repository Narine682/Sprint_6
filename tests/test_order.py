import pytest
import allure
from pages.main_page import MainPage
from data import BASE_URL

@allure.feature("Navigation")
class TestNavigation:
    @allure.title("Логотип Самоката возвращает на главную")
    def test_scooter_logo_navigates_home(self, driver):
        main = MainPage(driver)
        main.open_main(BASE_URL)
        main.click_order_bottom()
        main.click_scooter_logo()
        assert "qa-scooter.praktikum-services.ru" in driver.current_url, "Не открылось главный сайт"

    @allure.title("Логотип Яндекса открывает Dzen в новом окне")
    def test_yandex_logo_opens_dzen(self, driver):
        main = MainPage(driver)
        main.open_main(BASE_URL)
        main.click_yandex_logo()
        handles = driver.window_handles
        assert len(handles) >= 2, "Не открылось новое окно при клике на логотип Яндекса"
        driver.switch_to.window(handles[-1])
        assert "dzen.ru" in driver.current_url or "zen.yandex" in driver.current_url, "Не открылось Dzen"