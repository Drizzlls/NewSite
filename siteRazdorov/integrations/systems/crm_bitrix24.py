from bitrix24 import Bitrix24
import logging

logger = logging.getLogger(__name__)
class CRMBitrix24():
    __BX24 = Bitrix24('https://novoedelo.bitrix24.ru/rest/24/fhrx35sn7urhp0gj/')
    __STATUS_ID = 'UC_UR5RJI'
    def sendLeadBitrix24(self, data):
        try:
            send = self.__BX24.callMethod('crm.lead.add', fields={
                "STATUS_ID": self.__STATUS_ID,
                **data
            })
            logger.info(f'Данные отправлены в Битрикс24!')
            return send
        except Exception as e:
            logger.critical(f'Данные в Битрикс24 не отправлены! Ошибка - {e}')
            return False

