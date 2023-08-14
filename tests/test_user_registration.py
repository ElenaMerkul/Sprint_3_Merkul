from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators

class TestUserRegisration():

    def test_user_registration_correct_password_and_login(self, driver):
        name = "Елена"
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj']"))).text
        assert text == "Зарегистрироваться"


    def test_user_registration_password_less_than_6_fail(self, driver):
        name = "Елена"
        email = "merkulelena122@mail.ru"
        password = "1"

        driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(name)
        driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(By.XPATH, ".//button[contains(@class,'button_button_type_primary')]").click()

        error_pasword = driver.find_element(By.XPATH, ".//fieldset[3]/div/p").text
        assert error_pasword == "Некорректный пароль"

