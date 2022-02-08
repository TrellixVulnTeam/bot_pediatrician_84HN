# -*- coding: utf-8 -*-
import os
import telebot
from telebot import types

token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in [
        'ОРВИ/ОРЗ',
        'ГВ',
        'Витамин Д',
        'Паразитоз',
        'Анемия',
        'Аптечка',
        'Ожог',
        'Ушная боль',
        'Зубная боль',
        'Температура',
        'Запор',
        'Диарея/Рвота',
        'Сон',
        'Падение',
        'Онлайн консультация',
    ]])
    bot.send_message(m.chat.id, 'Выберите жалобу', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'ОРВИ/ОРЗ':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Сопли',
            'Красное горло',
            'Кашель',
        ]])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)
    elif message.text == 'ГВ':
        keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboardgostart.add(*[types.KeyboardButton(name) for name in [
            'Мало молока',
            'Лактостаз',
        ]])
        bot.send_message(message.chat.id, 'Выберите кнопку', reply_markup=keyboardgostart)
    elif message.text == 'Витамин Д':
        bot.send_message(message.chat.id, '''💜ВИТАМИН Д💜
        Дозировка для новорожденного до 6месяцев жизни на гв (при том что у мамы хороший уровень витамин Д и она профилактически продолжает принимать 1000ме):
        - С 6месяцев до 1,6тэто 1600ме.
        - Ближе к 2м годика это 2000ме,без анализа!!!!с анализами другие подсчеты.
    Аквадетримы,детримаксы,эвалары дети приходят с рахитом, перевозбужденные, не спящие.
    Дело Ваше, Вам виднее что и как и когда давать.''')
    elif message.text == 'Паразитоз':
        bot.send_message(message.chat.id, '''💜Подготовка к  исследованию на паразитоз.💜
        1) Пьете желчегонные - фламин, артишок,хофитол, шиповник, по инструкции, за полчаса до еды три раза в день около месяца.
        2) Примерно каждые  5-7-10 дней сдаете кал методами - парасеп, либо двойная седиментация, либо расширенное информативное копрологическое исследование Фарм-т(Казань).
        💜 Чтобы повысить вероятность нахождения сдавать в период угасающей луны, в этот период паразиты выходят.💜
        Ну а если нашли:
         💚оак с лейкоформулой
         💚оам
         💚копрограмма
         💚узи органов брюшной полости
         👣Если есть атопия, то эозинофильнокатионный белок, с-реактивный белок, ig E иммуноглобулин, чтобы отличить аллергию от паразитоза.
         💜Найдем причину и устраним вместе , обращайтесь на личную консультацию.''')


bot.polling()
