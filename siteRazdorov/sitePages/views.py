from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from bitrixAPI.views import DataBitrix24
from .models import Article


class IndexPage(View):
    """ Главная страница """
    template_name = 'pages/index.html'
    context = {
        'title' : 'Заполненный Title',
        'description' : 'Описание страницы',
        'namePage' : 'Название страницы для Битрикса'
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class AboutPage(View):
    """ Страница 'О нас' """
    template_name = 'pages/about.html'

    def get(self, request):
        return render(request, self.template_name)

class ArticlesPage(View):
    """ Страница 'Статьи' """
    template_name = 'pages/articles/articles.html'

    def get(self, request):
        return render(request, self.template_name)

class ArticlePage(View):
    """ Страница Определенной статьи """
    template_name = 'pages/articles/article.html'

    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        return render(request, self.template_name, {'article': article})

class ContactsPage(View):
    """ Страница 'Контакты' """
    template_name = 'pages/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

class CooperationPage(View):
    """ Страница 'Сотрудничество' """
    template_name = 'pages/cooperation.html'

    def get(self, request):
        return render(request, self.template_name)

class ReviewsPage(View):
    """ Страница 'Отзывы клиентов' """
    template_name = 'pages/reviews.html'

    def get(self, request):
        return render(request, self.template_name)

class CasesPage(View):
    """ Страница 'Завершенные дела' """
    template_name = 'pages/cases.html'

    def get(self, request):
        return render(request, self.template_name)

class FAQPage(View):
    """ Страница 'Основные вопросы' """
    template_name = 'pages/faq.html'

    def get(self, request):
        return render(request, self.template_name)


class CalcPage(View):
    """ Страница 'Калькулятор стоимости банкротства' """
    template_name = 'pages/calc.html'

    def get(self, request):
        return render(request, self.template_name)

class SalePage(View):
    """ Страница 'Скидки' """
    template_name = 'pages/sale.html'

    def get(self, request):
        return render(request, self.template_name)

class VacanciesPage(View):
    """ Страница 'Вакансии' """
    template_name = 'pages/vacancies.html'

    def get(self, request):
        return render(request, self.template_name)


def notFoundPage(request, *args, **kwargs):
    """ Страница '404' """
    return render(request, '404.html', status=404)
