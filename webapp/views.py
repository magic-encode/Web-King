from django.shortcuts import redirect, render

from webapp.libs.telegram import telebot

from webapp.forms import ContactForm



def home(request, _type: str = telebot.TYPE_ZAKAS):
    # form = ContactForm()
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         obj=form.save(commit=False)
    #         obj.save()
    #         text = f"<b>O'quvchi: {obj.name}</b>\n <b>O'quvchining yoshi: {obj.age}</b>\n <b>Kurs nomi: {obj.cours}</b>\n <b>Telefon raqami: {obj.numbers}</b>\n <b>Ota-Onanasining telefon raqami: {obj.numbers_parent}</b>\n <b>Yashash manzili: {obj.text}</b>\n"
    #         # text += f"<b>O'quvchining yoshi: {obj.age}</b>\n"
    #         # text += f"<b>Kurs nomi: {obj.cours}</b>\n"
    #         # text += f"<b>Telefon raqami: {obj.numbers}</b>\n"
    #         # text += f"<b>Ota-Onanasining telefon raqami: {obj.numbers_parent}</b>\n"
    #         # text += f"<b>Yashash manzili: {obj.text}</b>\n"
            
    #         telebot.send_message(text, _type)
    #         return redirect('home')

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

