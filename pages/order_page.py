from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPage(BasePage):
    locators = OrderPageLocators


    def fill_first_step(self, name, surname, address, metro, phone):
         self.send_keys(self.locators.NAME_INPUT,name)
         self.send_keys(self.locators.SURNAME_INPUT, surname)
         self.send_keys(self.locators.ADDRESS_INPUT, address)
         self.send_keys(self.locators.METRO_INPUT,metro)
         self.send_keys(self.locators.PHONE_INPUT, phone)




    def fill_second_step_and_confirm(self, rental_date="2025-10-07"):
        self.send_keys(self.locators.DELIVERY_DATE_INPUT, rental_date)
        self.click(self.locators.RENTAL_PERIOD_DROPDOWN)
        self.click(self.locators.RENTAL_DAYS_OPTION)
        self.click(self.locators.ORDER_BUTTON_FINAL)
        self.click(self.locators.CONFIRM_YES)


    def is_success_modal_visible(self):
        try:
            el = self.wait.until(EC.presence_of_element_located(self.locators.SUCCESS_MODAL))
            return el.is_displayed()
        except:
            return False