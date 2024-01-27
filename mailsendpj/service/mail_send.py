from ..entity.MailInfo import Mail
import logging
from smtplib import SMTP
from email.mime.text import MIMEText
import os


def send(mail_list: list[Mail]) -> None:
    logging.info("スプレッドシート認証処理")

    # SMTPサーバーを指定
    host = os.getenv("SMTP_HOST_NAME")
    port = os.getenv("SMTP_PORT")
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")

    with SMTP(
        host,
        port,
    ) as server:
        server.starttls()
        server.login(user, password)

        for mail in mail_list:
            msg = createMIMEText(mail)
            # server.send_message(msg)


def createMIMEText(mail: Mail) -> MIMEText:
    logging.info("MIMEText生成処理_mail.title=%s", mail.title)
    msg = MIMEText(mail.letter_body, "plain", "utf-8")
    msg["Subject"] = mail.title
    msg["From"] = os.getenv("FROM_USER")
    msg["To"] = mail.address
    return msg
