import tweepy
import regex
import array 
import os
import glob
from datetime import datetime, timedelta
from itertools import islice
import pandas as pd
import sys
import telebot
import time

#user_ids=[1273384503210160128, 1397450323963252739, 1344128267134119936, 1446813073218674691]
BOT_TOKEN ='5624874933:AAE1i7dY2gpbvQRkPiUt52MjXg3wM3Tk6BA'
BOT_TOKEN_0Y = '5490661913:AAF_9zOX7hxstoOEPAwG9mu5YPhnZjHiwhg'

id_fomo_cap = -1001673513120
id_0y = -1001885597188


def remove_control_characters(str):
    return regex.sub(r'\p{C}', '', str)



bot_fomo_cap = telebot.TeleBot(BOT_TOKEN)
bot_0y = telebot.TeleBot(BOT_TOKEN_0Y)

columns = ['date','infl_id', 'infl_handle' , 'infl_name', 'id_follow', 'account_username','account_name', 'decription', 'created_at','followers_count','tweet_count']
df = pd.read_csv('new_fol.csv', sep='\t', header = None, names = columns)
ids = df.id_follow.unique()

for id in ids: 
 uniq = df.loc[df['id_follow'] == id]
 infl_names = uniq.infl_name.tolist() 
 infl_handles = uniq.infl_handle.tolist()
 acc_usernames = uniq.account_username.tolist()
 acc_names = uniq.account_name.tolist()
 decriptions = uniq.decription.tolist()
 dates = uniq.created_at.tolist()
 
 if isinstance(decriptions[0], str):
  decription = decriptions[0] 
 else: 
  decription = str(decriptions[0]) 

 if len(infl_names) > 3:
  string = "Project: <a href='https://twitter.com/" + acc_usernames[0] + "'>" + acc_names[0] + "</a>\n"\
            + "created: " + dates[0] + "\n" + decription  + "\n"

  i = 0
  for infl_name in infl_names: 
   string = string + "<a href='https://twitter.com/" + infl_handles[i] + "'>" + infl_name + "</a>\n"
   i +=1    
  bot_fomo_cap.send_message(id_fomo_cap, string, parse_mode='html', disable_web_page_preview=True)
  bot_0y.send_message(id_0y, string, parse_mode='html', disable_web_page_preview=True)
  
  for a in range(0,10):
    #print(i)    
    time.sleep(1)
    a +=1  
          
  