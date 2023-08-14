import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.maximize_window()
    yield driver
    driver.quit()

