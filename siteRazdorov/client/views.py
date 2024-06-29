import pprint
from client.clientDB import SaveDB
from integrations.systems.crm_bitrix24 import CRMBitrix24
from .utils import UtilsMethods
from urllib import parse
from urllib.parse import parse_qs


class Client(SaveDB):
    def __init__(self, request: dict):
        self.request = request
        self.bitrix24 = CRMBitrix24()

    def clientAdd(self):
        """ Добавляем клиента """
        data = self.treatmentData()
        saveDB = self.clientSaveForDB(data=data)
        addBitrix24 = self.bitrix24.sendLeadBitrix24(data=data)


    def treatmentData(self) -> dict:
        """ Обрабатываем данные, которые получили на входе """
        query = parse.urlparse(self.request.META.get('HTTP_REFERER'))  ## Получаем путь страницы
        utmMarks = UtilsMethods.conversionUtmMakrs(parse_qs(query.query))  ## Достаем UTM
        dataFormRequest = UtilsMethods.dictionaryСonversion(self.request)  ## Получаем данные из request
        return {**utmMarks, **dataFormRequest}

