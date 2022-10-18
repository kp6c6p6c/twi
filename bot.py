#import time
#import eventlet
#import requests
#import logging
import telebot
#from time import sleep

BOT_TOKEN ='5624874933:AAE1i7dY2gpbvQRkPiUt52MjXg3wM3Tk6BA'
id = -1001673513120

bot = telebot.TeleBot(BOT_TOKEN)
text = ()
bot.send_message(id, '[link](example.com)', parse_mode = "Markdown", link_preview=False)
#bot.send_message(id, 'test')

#@bot.channel_post_handler(commands=['1001673513120'])
#
#def getid(message):
#    bot.send_message(message.chat.id, 'test')