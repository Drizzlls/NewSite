import pprint
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from urllib import parse
from urllib.parse import parse_qs
from bitrixAPI.views import DataBitrix24
from .models import Client as ClientDB


class Client:
    def __init__(self, request: dict):
        self.request = request
        self.clientDB = ClientDB

    def clientAdd(self):
        """ Добавляем клиента """
        data = self.treatmentData()
        pprint.pprint(data)
        saveDB = self.clientSaveForDB(data=data)

    def clientSaveForDB(self, data):
        """ Сохраняем клиента в базу """
        try:
            self.clientDB.objects.create(
                name = data['NAME'],
                phone = data['PHONE'][0]['VALUE'],
                ip = data['ipClient'],
                utm_source = data.get('UTM_SOURCE', ''),
                utm_medium = data.get('UTM_MEDIUM', ''),
                utm_campaign = data.get('UTM_CAMPAIGN', ''),
                utm_content = data.get('UTM_CONTENT', ''),
                utm_term = data.get('UTM_TERM', ''),
                transitionSource = data.get('referSite', ''),
                page = data.get('page', ''),
            )
            print('Сохранил')
        except Exception as e:
            print(f'Ошибка - {e}')


    def clientSendForBitrix24(self, data):
        """ Отправляем данные в Битрикс24 """
        pass

    def treatmentData(self) -> dict:
        """ Обрабатываем данные, которые получили на входе """
        query = parse.urlparse(self.request.META.get('HTTP_REFERER'))  ## Получаем путь страницы
        utmMarks = UtilsMethods.conversionUtmMakrs(parse_qs(query.query))  ## Достаем UTM
        dataFormRequest = UtilsMethods.dictionaryСonversion(self.request)  ## Получаем данные из request
        return {**utmMarks,**dataFormRequest}


class UtilsMethods:
    @staticmethod
    def dictionaryСonversion(request: dict) -> dict:
        """ Преобразование словаря """
        newDict = {}
        for k, v in request.POST.items():
            if k == "PHONE":
                newDict[k] = [{'VALUE': v, 'VALUE_TYPE': 'WORK'}]
            else:
                newDict[k] = v
        newDict['ipClient'] = newDict['ipClient'].strip('\n')
        newDict['page'] = request.META.get('HTTP_REFERER').split('?')[0]
        return newDict

    @staticmethod
    def conversionUtmMakrs(data: dict) -> dict:
        """ Преобразование словаря с UTM метками """
        utm = ['UTM_SOURCE', 'UTM_MEDIUM', 'UTM_CAMPAIGN', 'UTM_CONTENT',  'UTM_TERM']
        marks = {}
        for k,v in data.items():
            if k.upper() in utm:
                marks[k.upper()] = v[0]
        return marks

