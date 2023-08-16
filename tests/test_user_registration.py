from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import Locators

class TestUserRegisration():

    def test_user_registration_correct_password_and_login(self, driver):
        name = "Елена"
        email = "merkulelena122@mail.ru"
        password = "123456"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        text = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@class='Auth_link__1fOlj']"))).text
        assert text == "Зарегистрироваться"

        # понимаю, что это одноразовый тест, но в проекте генерация паролей и логинов - это дополнительное и необязательное задание.
        # В вебинаре посмотрела как добавлять такие функции, но пока не хватает времени


    def test_user_registration_password_less_than_6_fail(self, driver):
        name = "Елена"
        email = "merkulelena122@mail.ru"
        password = "1"

        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.BUTTON_REG).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.FORM_OF_LOGIN))
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()

        error_password = driver.find_element(*Locators.ERROR_PASWORD).text
        assert error_password == "Некорректный пароль"

