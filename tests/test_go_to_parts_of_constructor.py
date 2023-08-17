from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
class TestPartsOfConsructor():
    def test_go_to_part_of_buns(self, driver):
        driver.find_element(*Locators.PART_OF_BUNS).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_OF_BUNS)).text
        assert text == 'Булки'
    def test_go_to_part_of_sauces(self, driver):
        driver.find_element(*Locators.PART_OF_SAUSES).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_OF_SAUSES)).text
        assert text == 'Соусы'
    def test_go_to_part_of_filling(self, driver):
        driver.find_element(*Locators.PART_OF_TOPPINGS).click()
        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_OF_TOPPINGS)).text
        assert text == 'Начинки'

