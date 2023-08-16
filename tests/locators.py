from selenium.webdriver.common.by import By
class Locators:
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(@class,'button_button_type_primary')]") # Кнопка "Войти в аккаунт"
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']") # Поле name
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']") # Поле email
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']")  # Поле password
    BUTTON_REG = (By.LINK_TEXT, "Зарегистрироваться") # Кнопка "Зарегистрироваться"
    LINK_REGISTER = (By.XPATH, ".//a[@class='Auth_link__1fOlj']")
    LINK_LOGIN = (By.LINK_TEXT, "Войти") # Кнопка "Войти" в форме регистрации
    ERROR_PASWORD = (By.XPATH, "[contains(text(), 'Некорректный пароль']") # ошибка регистрации
    BUTTON_RECOVERY = (By.LINK_TEXT, "Восстановить пароль") # Кнопка "Восстановить пароль"
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, ".//nav/a/p") # Кнопка "Личный кабинет"
    BUTTON_LOGOUT = (By.XPATH, ".//button[text()='Выход']") # Кнопка "Выход" из личного кабинета
    PART_OF_BUNS = (By.XPATH, ".//span[contains(text(), 'Булки']") # Кнопка для перехода в раздел "Булочки"
    PART_OF_SAUSES = (By.XPATH, ".//span[contains(text(), 'Соусы']") # кнопка для перехода в раздел "Соусы"
    PART_OF_TOPPINGS = (By.XPATH, ".//span[contains(text(), 'Начинки']") # кнопка для перехода в раздел "Начинки"
    HEADER_OF_BUNS = (By.XPATH, ".//h2[contains(text(), 'Булки']")
    HEADER_OF_SAUSES = (By.XPATH, ".//h2[contains(text(), 'Соусы']")
    HEADER_OF_TOPPINGS = (By.XPATH, ".//h2[contains(text(), 'Начинки']")
    HEADER_OF_CONSTRUCTOR = (By.XPATH, ".//h1[contains(text(), 'Соберите бургер']")
    BUTTON_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']") # Кнопка "Конструктор"
    LOGO = (By.XPATH, ".//div[contains(@class,'logo')]") # Логотип
    FORM_OF_LOGIN = (By.CLASS_NAME, "Auth_login__3hAey") # форма для входа и регистрации

