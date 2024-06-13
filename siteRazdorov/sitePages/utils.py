from django.shortcuts import render, redirect
from django.views import View
from urllib import parse
from urllib.parse import parse_qs
from bitrixAPI.views import DataBitrix24


class FormHandler(View):
    bitrixData = DataBitrix24()
    """ UC_UR5RJI """
    def post(self, request):
        # print(request.POST)
        query = parse.urlparse(request.META.get('HTTP_REFERER')) ## Получаем путь страницы
        utmMarks = UtilsMethods.conversionUtmMakrs(parse_qs(query.query)) ## Достаем UTM
        dataFormRequest = UtilsMethods.dictionaryСonversion(request.POST) ## Получаем данные из request
        print(dataFormRequest)
        # self.bitrixData.addLead(data={**utmMarks, **dataFormRequest}) ## Отправляем в Битрикс24
        return redirect('index')


class UtilsMethods:
    @staticmethod
    def dictionaryСonversion(data):
        """ Преобразование словаря """
        newDict = {}
        for k, v in data.items():
            if k == "PHONE":
                newDict[k] = [{'VALUE': v, 'VALUE_TYPE': 'WORK'}]
            else:
                newDict[k] = v
        return newDict

    @staticmethod
    def conversionUtmMakrs(data):
        """ Преобразование словаря с UTM метками """
        utm = ['UTM_SOURCE', 'UTM_MEDIUM', 'UTM_CAMPAIGN', 'UTM_CONTENT',  'UTM_TERM']
        marks = {}
        for k,v in data.items():
            if k.upper() in utm:
                marks[k.upper()] = v[0]
        return marks