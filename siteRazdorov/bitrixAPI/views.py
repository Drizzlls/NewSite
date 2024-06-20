import pprint

from django.shortcuts import render
from bitrix24 import Bitrix24

class DataBitrix24:
    bx24 = Bitrix24('https://novoedelo.bitrix24.ru/rest/24/fhrx35sn7urhp0gj/')


    def getLead(self):
        pprint.pprint(self.bx24.callMethod('crm.lead.get', id=223382)['STATUS_ID'])

    def addLead(self, data):
        self.bx24.callMethod('crm.lead.add', fields={
            "STATUS_ID": "UC_UR5RJI",
            **data
        })
