import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestLogin():

    def test_login_on_the_main_page(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(Locators.BUTTON_LOGIN, 'Оформить заказ'))


    def test_login_through_personal_account(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN)).text
        assert text == "Сохранить"

    def test_login_through_registration_form(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.LINK_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.LINK_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(Locators.BUTTON_LOGIN, 'Оформить заказ'))

    def test_login_on_the_recovery_form(self, driver):
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.BUTTON_RECOVERY).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.LINK_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(Locators.BUTTON_LOGIN, 'Оформить заказ'))
