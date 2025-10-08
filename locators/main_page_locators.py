from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]") # кнопка "Заказать" в верхней части страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")  # кнопка "Заказать" внизу страницы
    SCOOTER_LOGO = (By.CLASS_NAME,"Header_LogoScooter__3lsAR") #логотип Самоката
    YANDEX_LOGO = (By.CLASS_NAME,"Header_LogoYandex__3TSOI") #Логотип яндекса
    FAQ_QUESTION = (By.CSS_SELECTOR, ".accordion__item") #блоки вопросов в разделе FAQ
    FAQ_QUESTION_BUTTON = (By.CSS_SELECTOR, ".accordion__button") # кнопка-стрелка для раскрытия ответа
    FAQ_ANSWER = (By.CSS_SELECTOR, ".accordion__panel") # текст ответа на вопрос
