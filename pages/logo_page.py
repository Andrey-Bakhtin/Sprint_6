import allure
from locators.base_locators import LogoLocators
from pages.base_page import BasePage
from urls import BASE_URL


class LogoPage(BasePage):
    
    URL = BASE_URL

    @allure.step('Перейти на страницу заказа, кликнув на кнопку Заказать')
    def click_order_button(self):
        self.click_element(LogoLocators.HEADER_ORDER_BUTTON)
    
    @allure.step('Кликнуть на логотип Самокат')
    def click_scooter_logo(self):
        self.click_element(LogoLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть на логотип Яндекс')
    def click_yandex_logo(self):
        self.click_element(LogoLocators.YANDEX_LOGO)

    @allure.step('Перейти на новую страницу')
    def switch_to_new_tab_and_wait_url(self, expected_url_part):
        self.switch_to_next_tab()
        self.wait_url_contains(expected_url_part)

    @allure.step('Проверить url текущей страницы')
    def check_opened_page(self):
        return self.get_current_url()
      
