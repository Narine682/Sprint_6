from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import OrderPageLocators

class OrderPage:
    locators = OrderPageLocators

    @classmethod
    def fill_first_step(cls, driver, name, surname, address, metro, phone):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(cls.locators.NAME_INPUT)
        )

        driver.find_element(*cls.locators.NAME_INPUT).send_keys(name)
        driver.find_element(*cls.locators.SURNAME_INPUT).send_keys(surname)
        driver.find_element(*cls.locators.ADDRESS_INPUT).send_keys(address)
        driver.find_element(*cls.locators.METRO_INPUT).send_keys(metro)
        driver.find_element(*cls.locators.PHONE_INPUT).send_keys(phone)

        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(cls.locators.NEXT_BUTTON)
        )
        next_button.click()

    @classmethod
    def fill_second_step_and_confirm(cls, driver, rental_date="2025-10-05"):
        date_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(cls.locators.DELIVERY_DATE_INPUT)
            )
        date_input.send_keys(rental_date)

        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        )
        dropdown.click()
        option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(cls.locators.RENTAL_DAYS_OPTION)
        )
        option.click()

        order_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(cls.locators.ORDER_BUTTON_FINAL)
        )
        order_button.click()

        confirm_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(cls.locators.CONFIRM_YES)
        )
        confirm_button.click()
    @classmethod
    def is_success_modal_visible(cls, driver):
        try:
            el = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(cls.locators.SUCCESS_MODAL)
            )

            return el.is_displayed()
        except:
            return False