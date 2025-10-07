from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
         self.driver.get(url)

    def finds(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()


    def send_keys(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        el.send_keys(text)

    def current_url(self):
        return self.driver.current_url

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self,handle):
        self.driver.switch_to.window(handle)
