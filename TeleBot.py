from telebot import types
from config import *
import datetime
from telebot_calendar import Calendar, RUSSIAN_LANGUAGE

calendar = Calendar(language=RUSSIAN_LANGUAGE)

client_dict = {"Коррекция формы и размеров груди": {1: "Консультация пластического хирурга",
             2: "Увеличение груди эндопротезами",
             3: "Удаление имплантов груди",
             4: "Мастопексия (подтяжка груди)",
             5: "Уменьшение груди"},
            "Липосакция, липомоделирование, липофилинг":
            {6: "Абдоминопластика",
             7: "Липосакция 1 зона",
             8: "Липофилинг ягодиц",
             9: "Липофилинг лица (все отделы)"}}

keyboard1 = types.InlineKeyboardMarkup()
text1 = ''
for key, value in client_dict['Коррекция формы и размеров груди'].items():
    keyboard1.add(types.InlineKeyboardButton(key, callback_data=f'service;{key}'))
    text1 += f'{key} - {value}\n'

keyboard2 = types.InlineKeyboardMarkup()
text2 = ''
for key, value in client_dict['Липосакция, липомоделирование, липофилинг'].items():
    keyboard2.add(types.InlineKeyboardButton(key, callback_data=f'service;{key}'))
    text2 += f'{key} - {value}\n'

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton(text='Коррекция формы и размеров груди', callback_data=('division;1')))
keyboard.add(types.InlineKeyboardButton(text='Липосакция, липомоделирование, липофилинг', callback_data=('division;2')))

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text='Добрый день, вас приветствует плaстическая клиника Бетельгейз.'
                                            'Можем предложить наши услуги:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('division'))
def query_handler(call):
    razdel = call.data.split(';')
    if razdel[1] == '1':
        bot.send_message(call.message.chat.id, text1, reply_markup=keyboard1)
    elif razdel[1] == '2':
        bot.send_message(call.message.chat.id, text2, reply_markup=keyboard2)


@bot.callback_query_handler(func=lambda call: call.data.startswith('service'))
def callback_inline(call):
    service = call.data.split(';')
    if service[1] == '1':
        bot.send_message(call.message.chat.id, text='Введите дату')
    elif service[1] == '2':
        bot.send_message(call.message.chat.id, text='Введите дату')

current_shown_dates = {}
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now()  # Current date
    chat_id = message.chat.id
    date = (now.year, now.month)
    current_shown_dates[chat_id] = date  # Saving the current date in a dict
    markup = create_calendar(now.year, now.month)
    bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
def get_day(call):
        chat_id = call.message.chat.id
        bot.register_next_step_handler(call, date_for, chat_id)
def date_for(chat_id, call):
    saved_date = current_shown_dates.get(chat_id)
    if (saved_date is not None):
        day = call.data[13:]
        date = datetime.date(int(saved_date[0]), int(saved_date[1]), int(day))
        bot.send_message(chat_id, str(date))
        bot.answer_callback_query(call.id, text="Выбрана дата")
        global str_date
        str_date = str(date)
        return date

    else:
        bot.send_message(chat_id, 'Ошибка')
        pass


bot.polling()
