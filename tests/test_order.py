import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL

@allure.feature("Order")
class TestOrder:

    @allure.title("Проверка успешного оформления заказа через верхнюю кнопку")
    def test_order_from_top_button(self, driver):
        main = MainPage(driver)
        order = OrderPage(driver)
        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_top()
        order.fill_first_step("Иван","Иванов","Москва, Тверская 1","Пушкинская", "+79990001111")
        order.fill_second_step_and_confirm("2025-10-07")
        assert order.is_success_modal_visible(), "Модальное окно подтверждения заказа не появилась"

    @allure.title("Проверка успешного оформления заказа через нижнюю кнопку")
    def test_order_from_bottom_button(self, driver):
        main = MainPage(driver)
        order = OrderPage(driver)
        main.open(BASE_URL)
        main.accept_cookies()
        main.click_order_bottom()
        order.fill_first_step("Мария","Сидорова", "Санкт_Петербург, Невский 10", "Адмиралтейская", "+78889992222")
        order.fill_second_step_and_confirm("2025-10-08")
        assert order.is_success_modal_visible(),"Модальное окно подтверждения заказа не появилось"
