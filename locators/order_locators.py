from selenium.webdriver.common.by import By


class OrderLocators:

    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')

    FOOTER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    STATION_LIST = (By.XPATH, ".//div[@class='select-search__select']")
    NAME_INPUT = (By.XPATH,'//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH,'//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH,'//input[@placeholder="* Адрес: куда привезти заказ"]')
    STATION_INPUT = (By.XPATH,'//input[@placeholder="* Станция метро"]')
    PHONE_INPUT = (By.XPATH,'//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH,'//button[text()="Далее"]')

    DATE_INPUT = (By.XPATH,'//input[@placeholder="* Когда привезти самокат"]')
    DURATION_INPUT = (By.XPATH,'//div[text()="* Срок аренды"]')
    DURATION_TWO_DAYS = (By.XPATH, "//div[text() = 'двое суток']")
    DURATION_THREE_DAYS = (By.XPATH, "//div[text() = 'трое суток']")
    BLACK_SCOOTER_CHECKBOX = (By.ID, "black")
    GREY_SCOOTER_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH,'//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]')
    
    CONFIRM_ORDER_POPUP_TITLE = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_CONFIRMED_POPUP = (By.XPATH, '//div[text()="Заказ оформлен"]')
  
