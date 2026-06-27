import allure
import pytest
from locators.question_locators import QuestionLocators
from helpers import AccordionData

QUESTION_DATA = [
    (QuestionLocators.QUESTIONS[0], QuestionLocators.ANSWERS[0], AccordionData.answers[0]),
    (QuestionLocators.QUESTIONS[1], QuestionLocators.ANSWERS[1], AccordionData.answers[1]),
    (QuestionLocators.QUESTIONS[2], QuestionLocators.ANSWERS[2], AccordionData.answers[2]),
    (QuestionLocators.QUESTIONS[3], QuestionLocators.ANSWERS[3], AccordionData.answers[3]),
    (QuestionLocators.QUESTIONS[4], QuestionLocators.ANSWERS[4], AccordionData.answers[4]),
    (QuestionLocators.QUESTIONS[5], QuestionLocators.ANSWERS[5], AccordionData.answers[5]),
    (QuestionLocators.QUESTIONS[6], QuestionLocators.ANSWERS[6], AccordionData.answers[6]),
    (QuestionLocators.QUESTIONS[7], QuestionLocators.ANSWERS[7], AccordionData.answers[7]),
]

@allure.feature("Вопросы о важном")
class TestAccordion:

    @allure.story("Проверка открытия ответа при клике на вопрос")
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_answer",
        QUESTION_DATA,
        ids=[f"q{i}" for i in range(len(QUESTION_DATA))]
    )
    def test_accordion_item_opens_content(self, questions_page, question_locator, answer_locator, expected_answer):
        with allure.step("Прокрутка к вопросу и клик по нему"):
            questions_page.get_answer(question_locator, answer_locator)

        with allure.step("Проверка текста ответа"):
            actual_text = questions_page.get_text_from_element(answer_locator)
            assert actual_text == expected_answer, (
                f"Ожидался ответ: {expected_answer}\n"
                f"Получено: {actual_text}"
            )
