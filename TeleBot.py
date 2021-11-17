from telebot import types
from config import *
import datetime
from telebot_calendar import Calendar, RUSSIAN_LANGUAGE

# calendar = Calendar(language=RUSSIAN_LANGUAGE)


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
keyboard.add(types.InlineKeyboardButton(text='О наc', callback_data=('division;3')))


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
    elif razdel[1] == '3':
        bot.send_message(call.message.chat.id, text="Медицинский центр основан в 1997г. Адрес: Беларусь, г Минск, ул. Ленина, 9. "
                                                    "Специализация центра — пластическая эстетическая хирургия.")

# price = {1: "Бесплатно", 2: "1300$", 3: "1200$", 4: "1200-1800$", 5: "1500$",
#          6: "1500-2000$", 7: "400$(от 2 до 4 зон - 380$)", 8: "470$", 9: "700$"}

keyboard01 = types.InlineKeyboardMarkup()
keyboard01.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price01;1')))
keyboard02 = types.InlineKeyboardMarkup()
keyboard02.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price02;2')))
keyboard03 = types.InlineKeyboardMarkup()
keyboard03.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price03;3')))
keyboard04 = types.InlineKeyboardMarkup()
keyboard04.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price04;4')))
keyboard05 = types.InlineKeyboardMarkup()
keyboard05.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price05;5')))
keyboard06 = types.InlineKeyboardMarkup()
keyboard06.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price06;6')))
keyboard07 = types.InlineKeyboardMarkup()
keyboard07.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price07;7')))
keyboard08 = types.InlineKeyboardMarkup()
keyboard08.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price08;8')))
keyboard09 = types.InlineKeyboardMarkup()
keyboard09.add(types.InlineKeyboardButton(text='Узнать цену', callback_data=('price09;9')))

@bot.callback_query_handler(func=lambda call: call.data.startswith('price01'))
def query_handler(call):
    price01 = call.data.split(';')
    if price01[1] == '1':
        bot.send_message(call.message.chat.id, text="Бесплатно")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price02'))
def query_handler(call):
    price02 = call.data.split(';')
    if price02[1] == '2':
        bot.send_message(call.message.chat.id, text="1300$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price03'))
def query_handler(call):
    price03 = call.data.split(';')
    if price03[1] == '3':
        bot.send_message(call.message.chat.id, text="1200$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price04'))
def query_handler(call):
    price04 = call.data.split(';')
    if price04[1] == '4':
        bot.send_message(call.message.chat.id, text="1200-1800$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price05'))
def query_handler(call):
    price05 = call.data.split(';')
    if price05[1] == '5':
        bot.send_message(call.message.chat.id, text="1500$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price06'))
def query_handler(call):
    price06 = call.data.split(';')
    if price06[1] == '6':
        bot.send_message(call.message.chat.id, text="1500-2000$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price07'))
def query_handler(call):
    price07 = call.data.split(';')
    if price07[1] == '7':
        bot.send_message(call.message.chat.id, text="400$(от 2 до 4 зон - 380$)")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price08'))
def query_handler(call):
    price08 = call.data.split(';')
    if price08[1] == '8':
        bot.send_message(call.message.chat.id, text="470$")

@bot.callback_query_handler(func=lambda call: call.data.startswith('price09'))
def query_handler(call):
    price09 = call.data.split(';')
    if price09[1] == '9':
        bot.send_message(call.message.chat.id, text="700$")


@bot.callback_query_handler(func=lambda call: call.data.startswith('service'))
def callback_inline(call):
    service = call.data.split(';')
    if service[1] == '1':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Sergey-Iulianovich.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,  # Идентификатор чата
            photo=img,  # Картинка
            caption="МЕЧКОВКИЙ СЕРГЕЙ ЮЛЬЯНОВИЧ - врач высшей квалификации, пластический хирург, "
     "победитель конкурса на обладание звания «Лучший врач-2007», обладает учёной степенью кандидата наук",  # Текст к картинки
            reply_markup=keyboard01  # Кнопки
        )
        # Закрываем картинку
        img.close()
    elif service[1] == '2':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург: ")
        img = open('Sergey-Iulianovich.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВКИЙ СЕРГЕЙ ЮЛЬЯНОВИЧ - врач высшей квалификации, пластический хирург, "
                    "победитель конкурса на обладание звания «Лучший врач-2007», обладает учёной степенью кандидата наук",
            reply_markup=keyboard02
        )
        img.close()
    elif service[1] == '3':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Avseenko-Igor.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="АВСЕЕНКО ИГОРЬ ВЛАДИМИРОВИЧ - действительный член Белорусского общества пластических, "
     "реконструктивных и эстетических хирургов; участник белорусских и зарубежных конгрессов и симпозиумов по актуальным вопросам",
            reply_markup=keyboard03
        )
        img.close()
    elif service[1] == '4':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Avseenko-Igor.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="АВСЕЕНКО ИГОРЬ ВЛАДИМИРОВИЧ - действительный член Белорусского общества пластических, "
                    "реконструктивных и эстетических хирургов; участник белорусских и зарубежных конгрессов и симпозиумов по актуальным вопросам",
            reply_markup=keyboard04
        )
        img.close()
    elif service[1] == '5':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Mechkovskii-Sergey-sergeevich-1.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВСКИЙ СЕРГЕЙ СЕРГЕЕВИЧ - пластический хирург, микрохирург, врач высшей квалификации. "
     "Участник белорусских и международных конференций и симпозиумов по актуальным вопросам пластической",
            reply_markup=keyboard05
        )
        img.close()
    elif service[1] == '6':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Mechkovskii-Sergey-sergeevich-1.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВСКИЙ СЕРГЕЙ СЕРГЕЕВИЧ - пластический хирург, микрохирург, врач высшей квалификации. "
                    "Участник белорусских и международных конференций и симпозиумов по актуальным вопросам пластической",
            reply_markup=keyboard06
        )
        img.close()
    elif service[1] == '7':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Vilchevski-st.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВСКИЙ СЕРГЕЙ СЕРГЕЕВИЧ - пластический хирург, микрохирург, врач высшей квалификации. "
                    "Участник белорусских и международных конференций и симпозиумов по актуальным вопросам пластической",
            reply_markup=keyboard07
        )
        img.close()
    elif service[1] == '8':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Vilchevski-st.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВСКИЙ СЕРГЕЙ СЕРГЕЕВИЧ - пластический хирург, микрохирург, врач высшей квалификации. "
                    "Участник белорусских и международных конференций и симпозиумов по актуальным вопросам пластической",
            reply_markup=keyboard08
        )
        img.close()
    elif service[1] == '9':
        bot.send_message(call.message.chat.id, text="На эту услугу у нас предоставляется врач-хирург:")
        img = open('Vilchevski-st.jpg', 'rb')
        bot.send_photo(
            chat_id=call.message.chat.id,
            photo=img,
            caption="МЕЧКОВСКИЙ СЕРГЕЙ СЕРГЕЕВИЧ - пластический хирург, микрохирург, врач высшей квалификации. "
                    "Участник белорусских и международных конференций и симпозиумов по актуальным вопросам пластической",
            reply_markup=keyboard09
        )
        img.close()

# current_shown_dates = {}
# @bot.message_handler(commands=['calendar'])
# def get_calendar(message):
#     now = datetime.datetime.now()  # Current date
#     chat_id = message.chat.id
#     date = (now.year, now.month)
#     current_shown_dates[chat_id] = date  # Saving the current date in a dict
#     markup = create_calendar(now.year, now.month)
#     bot.send_message(message.chat.id, "Пожалуйста, выберите дату", reply_markup=markup)
#
#
# @bot.callback_query_handler(func=lambda call: call.data[0:13] == 'calendar-day-')
# def get_day(call):
#         chat_id = call.message.chat.id
#         bot.register_next_step_handler(call, date_for, chat_id)
# def date_for(chat_id, call):
#     saved_date = current_shown_dates.get(chat_id)
#     if (saved_date is not None):
#         day = call.data[13:]
#         date = datetime.date(int(saved_date[0]), int(saved_date[1]), int(day))
#         bot.send_message(chat_id, str(date))
#         bot.answer_callback_query(call.id, text="Выбрана дата")
#         global str_date
#         str_date = str(date)
#         return date
#
#     else:
#         bot.send_message(chat_id, 'Ошибка')
#         pass

if __name__ == '__main__':
    bot.polling(none_stop=True)
