from django.shortcuts import render, redirect
from django.views import View
from urllib import parse
from urllib.parse import parse_qs


class FormHandler(View):
    def post(self, request):
        query = parse.urlparse(request.META.get('HTTP_REFERER'))
        print(parse_qs(query.query))
        print(f'пост - {request.POST}')
        return redirect('index')