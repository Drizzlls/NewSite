from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views, urls
from .views import IndexPage, AboutPage, NewsPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('about/', AboutPage.as_view(), name='about'),
    path('news/', NewsPage.as_view(), name='news'),

]
