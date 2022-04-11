import telebot
from telebot import types

#5243818570:AAETX2_VS-wuSwcyvp0jf8320QxFXg5bdFw

name = ''
surname = ''
age = 0

bot = telebot.TeleBot('5243818570:AAETX2_VS-wuSwcyvp0jf8320QxFXg5bdFw')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Привет":
         bot.reply_to(message, "Приветствую")
    elif message.text == 'Здарова':
        bot.reply_to(message, "и тебе не хворать")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Регистрация началась, ответьте пожалуйста на следующие вопросы, Как вас зовут?")
        bot.register_next_step_handler(message, reg_name)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Введите вашу фамилию")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Сколько вам лет?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, "Введите возраст числами")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data='no')
    keyboard.add(key_no)
    question = "Тебе " + str(age) + ' лет? И тебя зовут: ' + name + " " + surname + '?'
    bot.send_message(message.from_user.id, text = question, reply_markup = keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Приятно познакомиться! Теперь вы зарегестрированы")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Давай попробуем еще раз")
        bot.send_message(message.chat.id, "Регистрация началась, ответьте пожалуйста на следующие вопросы, Как вас зовут?")
        bot.register_next_step_handler(call.message, reg_name)
bot.infinity_polling()