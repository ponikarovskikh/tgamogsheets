from telebot import TeleBot, types
from telebot.util import quick_markup
from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot import types, TeleBot
from telebot.custom_filters import AdvancedCustomFilter
from sheetsscript import *
from amocrmscript import *



bot=TeleBot(token='7955421291:AAGz1wD0KqA6Gu0QCwZEhX6w3Yjw524hehs')

# products_factory = CallbackData('product_id', prefix='products')



@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.send_message(message.chat.id,text= "Это бот по уcлугам проведения банкротсва\n")
        markup = quick_markup({

                'Оставить Заявку🔔': {'callback_data': 'makerq'},
                'Справка🧾': {'callback_data': 'info'},

        }, row_width=1)
        bot.send_message(message.chat.id, "Выберите действие ", reply_markup=markup)

#keyboards
def menu_markup():
    return quick_markup({

                'Оставить Заявку🔔': {'callback_data': 'makerq'},
                'Справка🧾': {'callback_data': 'info'},

        }, row_width=1)
def back_markup():
        return  quick_markup({


                'Назад': {'callback_data': 'back'},

        }, row_width=1)
# dict
userdata={}
@bot.callback_query_handler(func=lambda callback:callback.data)
def product_one_callback(callback,*args):
        print(callback.message.chat.id)
        if callback.data=='info':
                bot.edit_message_text(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.id,
                        text=f'Справка\n'
                                 f'введите:'
                                 f'1)фио'
                                 f'2)компания'
                                 f'3)телефон'
                                 f'для отправки вашей заявки',
                        reply_markup=back_markup())
        if callback.data == 'back':
                bot.edit_message_text(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.id,
                        text='Выберите действие',
                        reply_markup=menu_markup())
        if callback.data == 'makerq':
            bot.send_message(callback.message.chat.id,'Введите Ваше Имя')
            bot.register_next_step_handler(message=callback.message,callback=getname_handler)
            bot.delete_message(callback.message.chat.id,callback.message.id,4)

@bot.message_handler(content_types=['text'])
def getname_handler(message):
    user_id = message.chat.id
    name = message.text
    # Проверяем, существует ли ключ user_id в словаре user_data
    if user_id not in userdata:
        userdata[user_id] = {}
    userdata[user_id]['name'] = name
    bot.send_message(message.chat.id, 'Введите вашу фамилию')
    bot.register_next_step_handler(message, getsurname_handler)



@bot.message_handler(content_types=['text'])
def getsurname_handler(message):
        surnmame = message.text
        userdata[message.chat.id]['surname'] = surnmame
        bot.send_message(message.chat.id, 'Введите вашу компанию:')
        bot.register_next_step_handler(message,getcompany_handler)

@bot.message_handler(content_types=['text'])
def getcompany_handler(message):
        company = message.text
        userdata[message.chat.id]['company'] = company
        bot.send_message(message.chat.id, 'Введите ваш номер телефона для обратной связи ')
        bot.register_next_step_handler(message,getphone_handler)

@bot.message_handler(content_types=['text'])
def getphone_handler(message):
        from datetime import datetime
        phone = message.text
        userdata[message.chat.id]['phone'] = phone
        userdata[message.chat.id]['time'] = datetime.now().strftime('%Y-%m-%d')
        bot.send_message(message.chat.id, 'Данные получены! \n'
                                          'Ожидайте уведомления о постановке в очередь\n'
                                          'для обработки нашими специалистами')
        # print(message)
        userdata[message.chat.id]['username'] = f'{message.from_user.username}'
        create_info_google_sheets(userdata,message.chat.id)
        create_task_crm(userdata,message.chat.id)

        # print(userdata)



bot.polling(none_stop=True)











# @bot.inline_handler(lambda query: query.query == 'text')
# def query_text(inline_query):
#     try:
#         r = types.InlineQueryResultArticle('1', 'Result', types.InputTextMessageContent('Result message.'))
#         r2 = types.InlineQueryResultArticle('2', 'Result2', types.InputTextMessageContent('Result message2.'))
#         bot.answer_inline_query(inline_query.id, [r, r2])
#     except Exception as e:
#         print(e)
# @bot.message_handler(func=lambеda m: True)
# def echo_all(message):
# 	bot.reply_to(message, message.text)
#
# # Обработчик для всех входящих сообщений
# @bot.message_handler(func=lambda message: True)
# def handle_all_messages(message):
#     # Проверяем, соответствует ли сообщение ожидаемому формату (например, текст должен быть числом)
#     if not message.text.isdigit():
#         # Если текст не является числом, отправляем сообщение о неправильном вводе
#         bot.reply_to(message, "Вы ввели что-то неправильное. Пожалуйста, введите число.")
#     else:
#         # Ваша логика обработки сообщения, если текст является числом
#         pass




















