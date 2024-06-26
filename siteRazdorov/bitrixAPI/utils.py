import pprint
from bitrix24 import Bitrix24

class DataBitrix24:
    bx24 = Bitrix24('https://novoedelo.bitrix24.ru/rest/24/fhrx35sn7urhp0gj/')

    def addLead(self, data):
        try:
            add = self.bx24.callMethod('crm.lead.add', fields={
                "STATUS_ID": "UC_UR5RJI",
                **data
            })
            print('Отправилось')
        except Exception as e:
            print('Ошибка', e)