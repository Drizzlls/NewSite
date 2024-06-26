from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views, urls

from django.conf import settings
from django.conf.urls.static import static

from .views import IndexPage, AboutPage, ArticlesPage,ContactsPage, CooperationPage, ReviewsPage, CasesPage, FAQPage, CalcPage, SalePage, VacanciesPage, ArticlePage, FormHandler, ThanksPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('about/', AboutPage.as_view(), name='about'),

    path('articles/', ArticlesPage.as_view(), name='articles'),
    path('articles/<str:slug>/', ArticlePage.as_view(), name='article'),

    path('contacts/', ContactsPage.as_view(), name='contacts'),
    path('cooperation/', CooperationPage.as_view(), name='cooperation'),
    path('reviews/', ReviewsPage.as_view(), name='reviews'),
    path('cases/', CasesPage.as_view(), name='cases'),
    path('faq/', FAQPage.as_view(), name='faq'),
    path('calculator/', CalcPage.as_view(), name='calculator'),
    path('sale/', SalePage.as_view(), name='sale'),
    path('vacancies/', VacanciesPage.as_view(), name='vacancies'),
    path('thanks/', ThanksPage.as_view(), name='thanks'),


    path('handler/', FormHandler.as_view(), name='handler'),
    path('ckeditor/', include('ckeditor_uploader.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'sitePages.views.notFoundPage'