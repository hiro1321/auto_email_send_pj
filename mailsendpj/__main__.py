from .service import parse_spreadsheet
from .service import mail_send
from . import settings


mail_list = parse_spreadsheet.get_mail_list()
mail_send.send(mail_list)
