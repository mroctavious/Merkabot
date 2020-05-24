import telebot
from traducciones import DICCIONARIO
from telebot import types

idioma="en"

##This function will read configuration file and set the options for the program to work
#config options can be defined by the user during runtime
def readConfigFile(configFilename):
    config = {}
    with open(configFilename, 'r') as f:
        lines = f.read().splitlines()
        for line in lines:
            if line.startswith("#") or "=" not in line:
                continue
            data=line.split("=")
            option=data[0].strip()
            value=data[1].strip()
            config[option]=value
    return config
#https://github.com/eternnoir/pyTelegramBotAPI

config=readConfigFile("Merkabot.cfg")

##Starting the bot
bot = telebot.TeleBot(config['BOT_TOKEN'])

#functions for /subProduct

def getProductCost(message, product_name, product_description):
    product_cost = message.text
    bot.reply_to(message, DICCIONARIO['cost_will_show'][idioma] + ": " + product_cost + "\n")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(DICCIONARIO['res_positiva'][idioma], DICCIONARIO['res_negativa'][idioma])
    bot.send_message(message.chat.id, DICCIONARIO['estas_seguro'][idioma] + "\n", reply_markup=markup)
    bot.register_next_step_handler(message, verifyProductCost, product_name, product_description, product_cost)

def verifyProductCost(message, product_name, product_description, product_cost):
    if message.text == DICCIONARIO['res_positiva'][idioma]:
        bot.reply_to(message, "TERMINAMOS :D")
        #bot.reply_to(message, DICCIONARIO['foto'][idioma]) agregar foto
        #bot.register_next_step_handler(message, getProductCost, product_name, product_description)
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(DICCIONARIO['res_positiva'][idioma], DICCIONARIO['res_negativa'][idioma])
        bot.reply_to(message, DICCIONARIO['cam_prod_cost'][idioma], reply_markup=markup) 
        bot.register_next_step_handler(message, verifyProductDescription, product_name, product_description )

def verifyProductDescription(message, product_name, product_description):
    if message.text == DICCIONARIO['res_positiva'][idioma]:
        bot.reply_to( message, DICCIONARIO['ingresa_cost'][idioma] )
        bot.register_next_step_handler(message, getProductCost, product_name, product_description)
        #bot.reply_to(message, DICCIONARIO['ingresa_descri'][idioma])
    else:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add(DICCIONARIO['res_positiva'][idioma], DICCIONARIO['res_negativa'][idioma])
        bot.reply_to(message, DICCIONARIO['cam_prod_descrip'][idioma], reply_markup=markup) 
        bot.register_next_step_handler(message, getAnswerProductDescrip, product_name )

def getProductDescription(message, product_name):
    product_description = message.text
    bot.reply_to(message, DICCIONARIO['aparecera_asi'][idioma] + ":\n\n" + product_description)
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(DICCIONARIO['res_positiva'][idioma], DICCIONARIO['res_negativa'][idioma])
    bot.send_message(message.chat.id, DICCIONARIO['estas_seguro'][idioma] + "\n", reply_markup=markup)
    bot.register_next_step_handler(message, verifyProductDescription, product_name, product_description)


def getAnswerProductDescrip(message, product_name):
    if message.text == DICCIONARIO['res_positiva'][idioma]:
        bot.reply_to(message, DICCIONARIO['ingresa_descri'][idioma])
        bot.register_next_step_handler(message, getProductDescription, product_name)
        #llevar a la siguiente function
    else:
        #adios!
        bot.reply_to(message, DICCIONARIO['despedida'][idioma])

def printAndVerifyProductName(message):
    product_name = message.text
    bot.reply_to(message, DICCIONARIO['aparecera_asi'][idioma] + ":\n\n" + product_name )
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(DICCIONARIO['res_positiva'][idioma], DICCIONARIO['res_negativa'][idioma])
    bot.send_message(message.chat.id, DICCIONARIO['estas_seguro'][idioma] + "\n", reply_markup=markup)
    bot.register_next_step_handler(message, getAnswerProductDescrip, product_name)


#Command /SubProduct
@bot.message_handler(commands=['subproduct'])
def productStart(message):
    bot.reply_to(message, DICCIONARIO['ingresa_prod'][idioma] + "\n")
    bot.register_next_step_handler(message, printAndVerifyProductName)

##Ejecutar el bot
bot.polling()

# sendMessage
#tb.send_message(chat_id, text)   ##DOMINADO


# All send_xyz functions which can take a file as an argument, can also take a file_id instead of a file.
# sendPhoto
#
#tb.send_photo(chat_id, photo)  ##DOMINADO
#tb.send_photo(chat_id, "FILEID")

#/ubi
# sendLocation
#20.618217, -100.397134
#tb.send_location(chat_id, lat, lon) 
