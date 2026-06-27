import allure
from pages.base_page import BasePage
from urls import BASE_URL


class QuestionsPage(BasePage):

    URL = BASE_URL

    @allure.step('Прокрутить до проверяемого вопроса')
    def scroll_to_questions(self, question):
        self.scroll_to_element(question)

    @allure.step('Кликнуть на вопрос')
    def click_question(self, question):
        self.click_element(question)

    @allure.step('Получить ответ на вопрос')
    def get_answer(self, question, answer):
        self.scroll_to_questions(question)
        self.click_question (question)
        self.wait_for_element (answer)
        answer_text = self.get_text_from_element(answer)
        return answer_text  
