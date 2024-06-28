import pprint
from urllib import parse
from urllib.parse import parse_qs
from client.clientDB import SaveDB
from integrations.systems.crm_bitrix24 import CRMBitrix24
import logging

logger = logging.getLogger(__name__)


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

