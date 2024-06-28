from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article
from client.views import Client


class IndexPage(View):
    """ Главная страница """
    template_name = 'pages/index.html'
    context = {
        'namePage': 'Главная страница'
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class AboutPage(View):
    """ Страница 'О нас' """
    template_name = 'pages/about.html'
    context = {

    }
    def get(self, request):
        return render(request, self.template_name, context=self.context)

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
        return render(request, self.template_name, {'article': article,
                                                    'title': article.title_page,
                                                    'description':article.description_page,
                                                    'namePage': article.name_page})

class ContactsPage(View):
    """ Страница 'Контакты' """
    template_name = 'pages/contacts.html'

    def get(self, request):
        return render(request, self.template_name)

class CooperationPage(View):
    """ Страница 'Сотрудничество' """
    template_name = 'pages/cooperation.html'

    context = {
        'namePage': 'Сотрудничество'
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)

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


class ThanksPage(View):
    """ Страница 'Спасибо' """
    template_name = 'pages/thanks.html'

    def get(self, request):
        return render(request, self.template_name)


def notFoundPage(request, *args, **kwargs):
    """ Страница '404' """
    return render(request, '404.html', status=404)


class FormHandler(View):

        def post(self, request):
            client = Client(request=request)
            client.clientAdd()
            return HttpResponse(True)
