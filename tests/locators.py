from selenium.webdriver.common.by import By
class Locators:
    BUTTON_LOGIN = (By.XPATH, ".//button[contains(@class,'button_button_type_primary')]") # Кнопка "Войти в аккаунт"
By.XPATH, ".//fieldset[2]/div/div/input" # Поле email
By.XPATH, ".//input[@type='password']" # Поле password
By.XPATH, ".//fieldset[1]/div/div/input" # Поле name
By.LINK_TEXT, "Зарегистрироваться" # Кнопка "Зарегистрироваться"
By.LINK_TEXT, "Войти" # Кнопка "Войти" в форме регистрации
By.LINK_TEXT, "Восстановить пароль" # Кнопка "Восстановить пароль"
By.XPATH, ".//nav/a/p" # Кнопка "Личный кабинет"
By.XPATH, ".//button[text()='Выход']" # Кнопка "Выход" из личного кабинета
By.XPATH, "//div[1]" # Кнопка для перехода в раздел "Булочки"
By.XPATH, "//div[1]/div[3]" # кнопка для перехода в раздел "Соусы"
By.XPATH, "//div[1]/div[3]" # кнопка для перехода в раздел "Начинки"
By.XPATH, ".//p[text()='Конструктор']" # Кнопка "Конструктор"
By.XPATH, ".//a/svg" # Логотип
By.CLASS_NAME, "Auth_login__3hAey" # форма для входа и регистрации
By.XPATH, "//ul[1]" # Раздел "Булочки"
By.XPATH, "//ul[2]" # Раздел "Соусы"
By.XPATH, "//ul[3]" # Раздел "Начинки"
