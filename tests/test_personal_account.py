from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators
class TestPersonalAccount():
    def test_go_to_personal_account(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        assert 'https://stellarburgers.nomoreparties.site/login' in driver.current_url
    def test_go_from_personal_account_to_logo(self, driver):
        driver.maximize_window()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.LOGO).click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_OF_CONSTRUCTOR)).text
        assert text == "Соберите бургер"
    def test_go_from_personal_account_to_constructor(self, driver):
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_OF_CONSTRUCTOR)).text
        assert text == "Соберите бургер"

    def test_go_out_from_personal_account(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGOUT))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN)).text
        assert text == "Войти"
