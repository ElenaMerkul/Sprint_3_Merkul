import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators

class TestLogin():

    def test_login_on_the_main_page(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(By.XPATH, ".//input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        time.sleep(3)
        # применила sleep, поскольку не проходила проверка
        # через WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(@class,'button_button_type_primary')]"))).text

        text = driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").text
        assert text == 'Оформить заказ'

    def test_login_through_personal_account(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(By.XPATH, ".//nav/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(By.XPATH, ".//nav/a/p").click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(@class,'button_button_type_primary')]"))).text
        assert text == "Сохранить"

    def test_login_through_registration_form(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Войти").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        time.sleep(3)
        # применила sleep, поскольку не проходила проверка
        # через WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(@class,'button_button_type_primary')]"))).text

        text = driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").text
        assert text == 'Оформить заказ'

    def test_login_on_the_recovery_form(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Войти").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        time.sleep(3)
        # применила sleep, поскольку не проходила проверка
        # через WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(@class,'button_button_type_primary')]"))).text

        text = driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").text
        assert text == 'Оформить заказ'
