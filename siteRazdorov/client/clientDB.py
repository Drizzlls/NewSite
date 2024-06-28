from client.models import Client as ClientDB
import logging

logger = logging.getLogger(__name__)

class SaveDB:
    clientDB = ClientDB
    def clientSaveForDB(self, data):
        """ Сохраняем клиента в базу """
        try:
            self.clientDB.objects.create(
                name=data['NAME'],
                phone=data['PHONE'][0]['VALUE'],
                ip=data['ipClient'],
                utm_source=data.get('UTM_SOURCE', ''),
                utm_medium=data.get('UTM_MEDIUM', ''),
                utm_campaign=data.get('UTM_CAMPAIGN', ''),
                utm_content=data.get('UTM_CONTENT', ''),
                utm_term=data.get('UTM_TERM', ''),
                transitionSource=data.get('referSite', ''),
                page=data.get('page', ''),
            )
            logger.info('Клиент сохранен в базу данных!')
        except Exception as e:
            logger.critical(f'Клиент не записался в базу! Ошибка - {e}')