import pprint
from django.test import TestCase, SimpleTestCase
class UtilsTest(TestCase, SimpleTestCase):
    """ Обработчик """

    TITLE = '<title> Банкротство физических лиц </title>'
    def htmlAndStatusCodeTest(self, response, template, status_code=200):
        self.assertTemplateUsed(response, template)
        self.assertNotContains(response, self.TITLE, status_code=200)

# class TestPages(UtilsTest):
    """ Проверка доступности страниц по адресам """
    # def test_index(self):
    #     """ Тест главной страницы """
    #     response = self.client.get('/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/index.html')
    #
    # def test_about(self):
    #     """ Тест страницы 'О нас' """
    #     response = self.client.get('/about/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/about.html')
    #
    # def test_articles(self):
    #     """ Тест страницы 'Статьи' """
    #     response = self.client.get('/articles/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/articles/articles.html')
    #
    # def test_contacts(self):
    #     """ Тест страницы 'Контакты' """
    #     response = self.client.get('/contacts/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/contacts.html')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_cooperation(self):
    #     """ Тест страницы 'Сотрудничество' """
    #     response = self.client.get('/cooperation/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/cooperation.html')
    #
    #
    # def test_reviews(self):
    #     """ Тест страницы 'Отзывы' """
    #     response = self.client.get('/reviews/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/reviews.html')
    #
    # def test_cases(self):
    #     """  Тест страницы 'Дела' """
    #     response = self.client.get('/cases/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/cases.html')
    #
    # def test_faq(self):
    #     """ Тест страницы 'Частые вопросы' """
    #     response = self.client.get('/faq/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/faq.html')
    #
    # def test_calculator(self):
    #     """ Тест страницы 'Калькулятор' """
    #     response = self.client.get('/calculator/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/calc.html')
    #
    # def test_sale(self):
    #     """ Тест страницы 'Скидки' """
    #     response = self.client.get('/sale/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/sale.html')
    #
    # def test_vacancies(self):
    #     """ Тест страницы 'Вакансии' """
    #     response = self.client.get('/vacancies/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/vacancies.html')
    #
    # def test_thanks(self):
    #     """ Тест страницы 'Спасибо' """
    #     response = self.client.get('/thanks/')
    #     self.htmlAndStatusCodeTest(response=response, template='pages/thanks.html')

    # def test_404_page(self):
    #     response = self.client.get('/404/')
    #     self.assertTrue(response.status_code == 404)




