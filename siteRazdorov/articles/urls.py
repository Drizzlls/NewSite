from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views, urls
from .views import ArticlesPage, ArticlePage

urlpatterns = [
    path('articles/', ArticlesPage.as_view(), name='articles'),
    path('articles/<str:slug>/', ArticlePage.as_view(), name='article'),


]
