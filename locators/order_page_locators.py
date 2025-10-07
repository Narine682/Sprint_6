from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя' ]")  # поле "Имя"
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")  # поле "Фамилия"
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # поле "Адрес"
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")  # поле выбора станции метро
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")  # поле телефона
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")  # кнопка "Далее" для перехода ко второму шагу

    # Второй шаг(пример)
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DAYS_OPTION = (
    By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='сутки']")  # выбор срока аренды "сутки"
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    ORDER_BUTTON_FINAL = (By.XPATH, "//button[text()='Заказать']")  # кнопка "Заказать" на втором шаге
    CONFIRM_YES = (By.XPATH, "//button[text()='Да']")  # кнопка подтверждения заказа в модальном окне
    SUCCESS_MODAL = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")  # модальное окно успешного создания заказа
