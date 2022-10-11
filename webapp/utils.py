import numbers
from webapp.libs.telegram import telebot

from .models import ContactModel


def send_message(mydict: dict, _type: str = telebot.TYPE_ZAKAS) -> None:

    if mydict is not None:
        text: str = ""

        obj = ContactModel.objects.create(
            name=mydict.get('name'),
            age=mydict.get('age'),
            cours=mydict.get('cours'),
            numbers=mydict.get('phone'),
            numbers_parent=mydict.get('numbers_parent'),
            text=mydict.get('text'),
        )
        
        text += f"<b>O'quvchi: {obj.name}</b>\n"
        text += f"<b>O'quvchining yoshi: {obj.age}</b>\n"
        text += f"<b>Kurs nomi: {obj.cours}</b>\n"
        text += f"<b>Telefon raqami: {obj.numbers}</b>\n"
        text += f"<b>Ota-Onanasining telefon raqami: {obj.numbers_parent}</b>\n"
        text += f"<b>Yashash manzili: {obj.text}</b>\n"

        context: dict = {
            "text": text,
            "_type": _type
        }

        telebot.send_message(**context)

