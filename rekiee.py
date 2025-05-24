import telebot
from telebot import types
import json
import os
import time

bot = telebot.TeleBot("6403082457:AAHdyXU6XeVgYd966VOhJ41FEk5rMRCIkYE")


if not os.path.isfile('users.json'):
    with open('users.json', 'w') as file:
        file.write('[]')

@bot.message_handler(commands=['start'])
def start(message):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        user_exists = False
        for user in users:
            if user.get("chat_id") == message.chat.id:
                user_exists = True
                break
        if not user_exists:
            users.append({"chat_id": message.chat.id, "losses": 0, "wins": 0})
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.reply_to(message, 'Напиши /Go. Чтоб узнать о Вязниках')

@bot.message_handler(commands=['Go'])
def ur(message):
    bot.reply_to(message, 'Хочешь начать?', reply_markup=get_join_channel_keyboard())
def get_join_channel_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton('Уровень 1', callback_data='join_channel')
    keyboard.add(button1)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'В небо взмыла стелла эта, \nС барельефов, как с портретов, \nСмотрят на огонь солдаты, \nЧто с войны пришли когда-то.\nИмена на звездах знает\nУ нас каждый горожанин. \nБольше всех у нас героев - \nДвадцать пять в войну и трое, \nКто имеет это званье. \nУ аллеи той названье\nЕсть, конечно, вы тут правы, \nИ она...', reply_markup=get_join_channel_RE())
def get_join_channel_RE():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re3 = types.InlineKeyboardButton('Аллея Славы и Воинский мемориал', callback_data='join_re3')
    re4 = types.InlineKeyboardButton('Введенский мужской монастырь', callback_data='join_re4')
    reki2.add(re3, re4)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re3')
def dont_join_channel(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None) 
    bot.send_photo(call.message.chat.id, open('Rost.jpg', 'rb'))
    bot.send_location(call.message.chat.id, 56.246046, 42.139185)
    bot.send_message(call.message.chat.id, "Прогулочная зона, мемориальный музей под открытым небом и архитектурно-ландшафтный комплекс – одно из самых узнаваемый и популярных у туристов мест в Вязниках. Аллея славы была заложена к 30-летнему юбилею Победы, в мае 1975. Центральным объектом на ней стала установленная тогда же величественная стела с барельефом, возле которой горит Вечный огонь. Автором памятника стал мастер из города Горького В.Ф. Трондин.")
    bot.send_message(call.message.chat.id, "Правильно! Хочешь начать новый уровень?", reply_markup=get_join_channel_keyboard3())

@bot.callback_query_handler(func=lambda call: call.data == 'join_re4')
def dont_join_channel_redd(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE())

def get_join_channel_keyboard3():
    keyboard = types.InlineKeyboardMarkup()
    button3 = types.InlineKeyboardButton('Уровень 2', callback_data='join_channel2')
    keyboard.add(button3)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel2')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'Есть музеев много разных, \nИ по своему прекрасных, \nНо такой один в России, И не просто он красивый. \nЖил поэт когда-то в нем, \nНо тогда был просто дом. \nА теперь всем интересно \nПосетить музей наш...', reply_markup=get_join_channel_RE2())
def get_join_channel_RE2():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re5 = types.InlineKeyboardButton('Музей песни ХХ века', callback_data='join_re5')
    re6 = types.InlineKeyboardButton('Дача Татаринцева', callback_data='join_re6')
    reki2.add(re5, re6)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re5')
def dont_join_channel(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None) 
    bot.send_photo(call.message.chat.id, open('120.jpg', 'rb'))
    bot.send_location(call.message.chat.id, 56.246964, 42.156880)
    bot.send_message(call.message.chat.id, "Прославленный деятель появился на свет в селе Малое Петрино, что располагалось в черте нынешних Вязников. Отец поэта-песенника был состоятельным и достаточно известным в этой местности предпринимателем и торговцем. На собственные средства Иван Фатьянов построил здание, где разместился его торговый дом и заведения для досуга горожан – кинематограф и библиотека.")
    bot.send_message(call.message.chat.id, "Правильно! Хочешь начать новый уровень?", reply_markup=get_join_channel_keyboard4())
@bot.callback_query_handler(func=lambda call: call.data == 'join_re6')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE2())

def get_join_channel_keyboard4():
    keyboard = types.InlineKeyboardMarkup()
    button4 = types.InlineKeyboardButton('Уровень 3', callback_data='join_channel3')
    keyboard.add(button4)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel3')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'На холме над Клязьмой-речкой \nЕсть известное местечко \nГрад стоял в былое времяДолгорукого-то брат \nОсновал тогда тот град\nЗащитить чтоб Русь помочь /nСлавный город....', reply_markup=get_join_channel_RE3())
def get_join_channel_RE3():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re7 = types.InlineKeyboardButton('Музей истории Вязниковского спорта', callback_data='join_re7')
    re8 = types.InlineKeyboardButton('Городище Ярополч-Залесский', callback_data='join_re8')
    reki2.add(re7, re8)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re7')
def dont_join_channel(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE3())
@bot.callback_query_handler(func=lambda call: call.data == 'join_re8')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None) 
    bot.send_photo(call.message.chat.id, open('L_height.webp', 'rb'))
    bot.send_location(call.message.chat.id, 56.235564, 42.243205)
    bot.send_message(call.message.chat.id, "Историческим предшественником Вязников, считается Ярополч-Залесский, основанный ещё в XI веке на правом берегу реки Клязьмы, примерно в пяти километрах от современного города. В названии отразилось имя основателя – князя Ярополка Владимировича, который приходился братом Юрию Долгорукому.")
    bot.send_message(call.message.chat.id, "Правильно! Хочешь начать новый уровень?", reply_markup=get_join_channel_keyboard5())

def get_join_channel_keyboard5():
    keyboard = types.InlineKeyboardMarkup()
    button5 = types.InlineKeyboardButton('Уровень 4', callback_data='join_channel4')
    keyboard.add(button5)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel4')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'Кто не знает песен этих \nРазошлись они по свету\nПро тальянку, соловьёв, \nОчень много добрых слов \nПро родной свой край писал, \nОн тогда того не знал, \nЧто площадку для торжеств \nВозведут, с неё окрест/nВидно Пётрино родное\nИ заречье заливное. \nЗдесь гостей на праздник ждут, Что...', reply_markup=get_join_channel_RE4())
def get_join_channel_RE4():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re9 = types.InlineKeyboardButton('Фатьяновский парк', callback_data='join_re9')
    re10 = types.InlineKeyboardButton('Памятник В.Н. Кубасову', callback_data='join_re10')
    reki2.add(re9, re10)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re9')
def dont_join_channel(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None) 
    bot.send_photo(call.message.chat.id, open('sczena.png', 'rb'))
    bot.send_location(call.message.chat.id, 56.247389, 42.134434)
    bot.send_message(call.message.chat.id, "Алексей Иванович Фатьянов – уроженец Вязниковского района; поэт, воспевавший родные места. Фатьянов пробыл на фронте всю Великую Отечественную войну, и после демобилизации сразу навестил Вязники. В 1962 году был сформирован Фатьяновский лесопарк.")
    bot.send_message(call.message.chat.id, "Правильно. Хочешь начать новый уровень?", reply_markup=get_join_channel_keyboard7())
    
@bot.callback_query_handler(func=lambda call: call.data == 'join_re10')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE4())

def get_join_channel_keyboard7():
    keyboard = types.InlineKeyboardMarkup()
    button100 = types.InlineKeyboardButton('Уровень 5', callback_data='join_channel5')
    keyboard.add(button100)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel5')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'В городе известней места \nНе найти, вы уж поверьте. \nДля души вид и для фото \nИли погулять охота. \nПокоритель всех сердец - Наш красивейший...', reply_markup=get_join_channel_RE55())
def get_join_channel_RE55():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re10 = types.InlineKeyboardButton('Смотровая площадка «Венец»', callback_data='join_re50')
    re11 = types.InlineKeyboardButton('Памятник коту ученому', callback_data='join_re51')
    reki2.add(re10, re11)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re50')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    bot.send_photo(call.message.chat.id, open('Klaz.jpg', 'rb'))
    bot.send_location(call.message.chat.id, 56.254488, 42.178923)
    bot.send_message(call.message.chat.id, "Река Клязьма, на правом берегу которой расположился город Вязники, — приток Оки. Со времен средневековья являлась важнейшей транспортной артерией. Берет своё начало на Московской возвышенности, протекая в самом сердце русских земель, по территории четырех регионов. Клязьма в районе Вязников – это удивительной красоты виды исконно русской природы в сочетании с духом древней истории, которой буквально источают речные берега.")
    bot.send_message(call.message.chat.id, "Правильно! Хочешь начать новый уровень?", reply_markup=get_join_channel_keyboard66())

@bot.callback_query_handler(func=lambda call: call.data == 'join_re51')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE55())

def get_join_channel_keyboard66():
    keyboard = types.InlineKeyboardMarkup()
    button100 = types.InlineKeyboardButton('Уровень 6', callback_data='join_channel6')
    keyboard.add(button100)
    return keyboard

@bot.callback_query_handler(func=lambda call: call.data == 'join_channel6')
def dont_join_channel(call):
    bot.send_message(call.message.chat.id, 'Бюст поставлен неслучайно - \nЭто человек отчаянный. \nВ космосе не раз бывал, \nЗемляков не забывал. \nБыл одним из летных асов - Лётчик-космонавт...', reply_markup=get_join_channel_RE6())
def get_join_channel_RE6():
    reki2 = types.InlineKeyboardMarkup(row_width=1)
    re10 = types.InlineKeyboardButton('Памятник коту ученому', callback_data='join_re60')
    re11 = types.InlineKeyboardButton('Памятник Алексею Фатьянову', callback_data='join_re62')
    re12 = types.InlineKeyboardButton('Памятник В.Н. Кубасову', callback_data='join_re61')
    reki2.add(re10, re11, re12)
    return reki2

@bot.callback_query_handler(func=lambda call: call.data == 'join_re61')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['wins'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)

    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    bot.send_photo(call.message.chat.id, open('images (6).jpg', 'rb'))
    bot.send_location(call.message.chat.id, 56.245162, 42.136587)
    bot.send_message(call.message.chat.id, "Бюст земляку, трижды покорившему космос, созданный авторами А. Елецким и Г. Постниковым, установили в 1983 году.")
    bot.send_message(call.message.chat.id, f"Победы - {user['wins']}, поражения - {user['losses']}")
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] = 0
                user['wins'] = 0
                break
        file.seek(0)
        json.dump(users, file, indent=4)

@bot.callback_query_handler(func=lambda call: call.data == 'join_re60')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE6())
@bot.callback_query_handler(func=lambda call: call.data == 'join_re62')
def dont_join_channel_re2(call):
    with open('users.json', 'r+') as file:
        users = json.load(file)
        for user in users:
            if user['chat_id'] == call.message.chat.id:
                user['losses'] += 1
                break
        file.seek(0)
        json.dump(users, file, indent=4)
    bot.send_message(call.message.chat.id, "Не правильно попробуй ещё раз!", reply_markup=get_join_channel_RE6())


bot.infinity_polling()
