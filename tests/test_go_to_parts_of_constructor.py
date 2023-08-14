from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class TestPartsOfConsructor():
    def test_go_to_part_of_buns(self, driver):
        driver.find_element(By.XPATH, "//div[1]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[1]")))

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[1]"))).text
        assert text == 'Булки'
    def test_go_to_part_of_sauces(self, driver):
        driver.find_element(By.XPATH, "//div[1]/div[3]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[2]")))

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[2]"))).text
        assert text == 'Соусы'
    def test_go_to_part_of_filling(self, driver):
        driver.find_element(By.XPATH, "//div[1]/div[3]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//ul[3]")))

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[3]"))).text
        assert text == 'Начинки'

