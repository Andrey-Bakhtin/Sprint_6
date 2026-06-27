from selenium.webdriver.common.by import By


class LogoLocators:
    
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']")
    SCOOTER_LOGO = (By.XPATH, ".//img[@alt='Scooter']")
    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
