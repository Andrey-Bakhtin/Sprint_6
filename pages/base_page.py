import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_locators import OrderLocators


class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) 
    
    @allure.step('Открыть страницу по url')
    def open(self):
        self.driver.get(self.URL)
    
    @allure.step('Принять cookie')
    def accept_cookies(self):
        if self.driver.find_element(*OrderLocators.COOKIE_BUTTON):
            self.driver.find_element(*OrderLocators.COOKIE_BUTTON).click()

    @allure.step('Проверить отображение элемента')
    def is_element_displayed(self, locator):
        try:
            return self.wait_for_element(locator).is_displayed()
        except:
            return False

    @allure.step('Ожидать элемент')
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.element_to_be_clickable(locator))
        return element
    
    @allure.step('Заполнить поле')
    def send_keys_to_field(self, locator, keys):
        field = self.wait_for_element(locator)
        return field.send_keys(keys)

    @allure.step('Получить текст')
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url
    
    @allure.step('Переключиться на новую вкладку')
    def switch_to_next_tab(self):
        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[-1])

    @allure.step('Ожидать появления части url')
    def wait_url_contains(self, url_part):
        return self.wait.until(EC.url_contains(url_part))
    
