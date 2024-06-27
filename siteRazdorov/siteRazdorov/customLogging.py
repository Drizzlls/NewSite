import logging




class TelegramHandler(logging.Handler):

    def emit(self, record):
        log_entry = self.format(record)
        print('я вошел в свой логгер!', log_entry)