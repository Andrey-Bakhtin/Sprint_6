import allure
from urls import BASE_URL


class TestLogo:
    
    @allure.title('При клике на логотип Самоката переход на главную страницу')
    def test_click_scooter_logo_opens_main_page(self, logo_page):
        logo_page.click_order_button()
        logo_page.click_scooter_logo()
        assert logo_page.check_opened_page() == f"{BASE_URL}/"

    @allure.title('При клике на логотип Яндекс переход на главную страница Дзена')
    def test_if_click_yandex_logo_dzen_page_opens(self, logo_page):
        logo_page.click_yandex_logo()
        logo_page.switch_to_next_tab()
        logo_page.wait_url_contains("dzen.ru")
        assert "dzen.ru" in logo_page.check_opened_page()
