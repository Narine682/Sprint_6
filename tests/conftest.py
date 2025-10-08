import pytest
import sys
import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
@pytest.fixture(scope="function")
def driver():
    options = Options()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

