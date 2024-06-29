from django.test import TestCase
from django.urls import reverse
from sitePages.tests import UtilsTest


class TestPages(UtilsTest):
    TITLE = '<title> Банкротство физических лиц </title>'

    def test_articles(self):
        """ Тест страницы 'Статьи' """
        response = self.client.get(reverse('articles'))
        self.htmlAndStatusCodeTest(response=response, template='article/articles/articles.html')

