from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views, urls
from .views import IndexPage, AboutPage, ArticlesPage,ContactsPage, CooperationPage, ReviewsPage, CasesPage, FAQPage, CalcPage, SalePage, VacanciesPage
from .utils import FormHandler

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('about/', AboutPage.as_view(), name='about'),
    path('news/', ArticlesPage.as_view(), name='news'),
    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('cooperation/', CooperationPage.as_view(), name='cooperation'),
    path('reviews/', ReviewsPage.as_view(), name='reviews'),
    path('cases/', CasesPage.as_view(), name='cases'),
    path('faq/', FAQPage.as_view(), name='faq'),
    path('calculator/', CalcPage.as_view(), name='calculator'),
    path('sale/', SalePage.as_view(), name='sale'),
    path('vacancies/', VacanciesPage.as_view(), name='vacancies'),
    path('handler/', FormHandler.as_view(), name='handler'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
handler404 = 'sitePages.views.notFoundPage'