import logging
import os
from google.oauth2.service_account import Credentials
import gspread
from ..entity.MailInfo import Mail


SHEET_KEY_MAIL = "メールアドレス"
SHEET_KEY_TITLE = "件名"
SHEET_KEY_BODY = "本文"


def get_mail_list() -> list[Mail]:
    gc = sheet_connection()
    mail_list = get_mail_info(gc)
    return mail_list


def sheet_connection() -> gspread.client.Client:
    logging.info("スプレッドシート認証処理")
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    print(os.getenv("AUTH_JSON_PATH"))
    credentials = Credentials.from_service_account_file(
        os.getenv("AUTH_JSON_PATH"), scopes=scopes
    )
    gc = gspread.authorize(credentials)
    return gc


def get_mail_info(gc: gspread.client.Client) -> list[Mail]:
    logging.info("スプレッドシート読み込み処理")
    # スプレッドシート情報を取得
    sheet = gc.open_by_url(os.getenv("SHEET_URL"))
    records = sheet.sheet1.get_all_records()

    # mailオブジェクトに格納
    mail_list = []
    for record in records:
        e = Mail(
            record.get(SHEET_KEY_MAIL),
            record.get(SHEET_KEY_TITLE),
            record.get(SHEET_KEY_BODY),
        )
        mail_list.append(e)

    return mail_list
