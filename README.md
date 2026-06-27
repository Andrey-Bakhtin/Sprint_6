UI‑автотесты для веб‑приложения «Самокат»
(Python + Selenium + Pytest + Allure, Mozilla Firfox 152.0.1) 

Структура проекта:
urls.py — URL приложения.
requirements.txt — зависимости.
helpers.py — генерация тестовых данных, класс с ожижаемымыми ответами.
conftest.py — фикстуры.
test_*.py — тестовые сценарии.
pages/ — классы страниц.
locators/ — локаторы элементов.

Реализованные тесты:
1. Логотипы: клик на «Самокат» (переход на главную страницу), клик на Яндекс (открытие Дзена в новой вкладке).
2. Оформление заказа: заполнение форм, выбор параметров, проверка сообщения «Заказ оформлен».
3. Раздел «Вопросы о важном»: проверка соответствия вопросов и ответов.

Установка зависимостей:
pip install -r requirements.txt

Запуск всех тестов:
pytest -v

Запуск конкретного теста:
pytest tests/test_logo_page.py -v
pytest tests/test_order_page.py -v
pytest tests/test_questions_page.py -v

Отчёт Allure:
pytest --alluredir=allure-results allure serve allure-results
