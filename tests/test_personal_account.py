from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from locators import Locators
class TestPersonalAccount():
    def test_go_to_personal_account(self, driver):
        driver.find_element(By.XPATH, ".//nav/a/p").click()
        assert 'https://stellarburgers.nomoreparties.site/login' in driver.current_url
    def test_go_from_personal_account_to_logo(self, driver):
        driver.maximize_window()
        driver.find_element(By.XPATH, ".//nav/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, "html/body/div/div/header/nav/div").click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[1]/h1"))).text
        assert text == "Соберите бургер"
    def test_go_from_personal_account_to_constructor(self, driver):
        driver.find_element(By.XPATH, ".//nav/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".text_type_main-large")))

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//section[1]/h1"))).text
        assert text == "Соберите бургер"

    def test_go_out_from_personal_account(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(By.XPATH, ".//nav/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))
        driver.find_element(By.XPATH, ".//input").send_keys(email)
        driver.find_element(By.XPATH, ".//input[@type='password']").send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(By.XPATH, ".//nav/a/p").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[text()='Выход']")))
        driver.find_element(By.XPATH, ".//button[text()='Выход']").click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey")))

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//button[contains(@class,'button_button_type_primary')]"))).text
        assert text == "Войти"
