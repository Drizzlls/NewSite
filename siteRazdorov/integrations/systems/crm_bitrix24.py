from bitrix24 import Bitrix24
import logging
from integrations.models import IntegrationsHook

logger = logging.getLogger('site')
class CRMBitrix24():

    def __init__(self):
        self.hook = IntegrationsHook.objects.get(title__title='Битрикс24').hook
        self.bx24 = Bitrix24(self.hook)
        self.status_id = 'UC_UR5RJI'


    def sendLeadBitrix24(self, data):
        try:
            send = self.bx24.callMethod('crm.lead.add', fields={
                "STATUS_ID": self.status_id,
                **data
            })
            logger.info(f'Данные отправлены в Битрикс24!')
            return send
        except Exception as e:
            logger.critical(f'Данные в Битрикс24 не отправлены! Ошибка - {e}')
            return False


