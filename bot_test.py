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


today = str(datetime.today().date())
yesterday = str(datetime.today().date() - timedelta(days=1))


files = []
files_count = 0
#print(files_count)
#files = glob.glob()
i = 0
#file_all_acc = open("new_fol.csv",'w')
#file_all_acc.close()
    
if len (sys.argv) > 1:
 twi_ac_filename = sys.argv[1]
else:
 print ("дай оргументов!")

df = pd.read_csv(twi_ac_filename, sep = '\t')
twi_ac_id = df['id'].tolist()
twi_ac_handle = df['handle'].tolist()
twi_ac_name = df['name'].tolist()
i=0


bot = telebot.TeleBot(BOT_TOKEN)
bot_0y = telebot.TeleBot(BOT_TOKEN_0Y)

user_couter = 0
for user_id in twi_ac_id:
 filename = str(user_id) + "_" + today + '_new.csv'
 columns = ['date','inf_id','inf_handle', 'inf_name', 'id_follow', 'account_username','account_name', 'decription', 'created_at','followers_count','tweet_count']
 
 df = pd.read_csv(filename, sep='\t', header = None, names = columns)
 df1 = pd.read_csv('new_fol.csv', sep='\t', header = None, names = columns)
 if len(df) > 0:
  user_names = df['account_name'].tolist()
  accounts = df['account_username'].tolist()
  decriptions = df['decription'].tolist()
  created = df['created_at'].tolist()
  followers = df['followers_count'].tolist() 
  tweets = df['tweet_count'].tolist()
  ids = df['id_follow'].tolist()
  i=0
  #print(accounts)

  for account in accounts:  
   print(twi_ac_handle[user_couter])
   accs = df1.loc[df1['id_follow'] == ids[i]].inf_name
   acc_string = ' and also: '
   for acc in accs:
    acc_string = acc_string  + acc + ", "
    l = len(acc_string)
   acc_string = acc_string[:l-2]    
 
#   print("<b><a href='https://twitter.com/" + str(account) + "'>" + str(user_names[i]) + '</a></b>\n'\
#                    +  'created: '  + str(created[i]) + '\nfollowers: ' + str(followers[i]) + ' tweets: ' + str(tweets[i]) + '\n'\
#                    + str(decriptions[i]) \
#                    + "\n<b>followed by <a href='https://twitter.com/" + str(twi_ac_handle[user_couter]) + "'>"\
#                    + str(twi_ac_name[user_couter]) + '</a></b>' + acc_string +"\n\n\n")
#   input("Press Enter to continue...")
   bot.send_message(id_fomo_cap,"\n<b><a href='https://twitter.com/" + str(account) + "'>" + str(user_names[i]) + '</a></b>\n'\
                    +  'created: '  + str(created[i]) + '\nfollowers: ' + str(followers[i]) + ' tweets: ' + str(tweets[i]) + '\n\n'\
                    + str(decriptions[i]) \
                    + "\n\n<b>followed by <a href='https://twitter.com/" + str(twi_ac_handle[user_couter]) + "'>"\
                    + str(twi_ac_name[user_couter]) + '</a></b>' + acc_string,\
                    parse_mode='html', disable_web_page_preview=True )
   bot_0y.send_message(id_0y,"\n<b><a href='https://twitter.com/" + str(account) + "'>" + str(user_names[i]) + '</a></b>\n'\
                    +  'created: '  + str(created[i]) + '\nfollowers: ' + str(followers[i]) + ' tweets: ' + str(tweets[i]) + '\n\n'\
                    + str(decriptions[i]) \
                    + "\n\n<b>followed by <a href='https://twitter.com/" + str(twi_ac_handle[user_couter]) + "'>"\
                    + str(twi_ac_name[user_couter]) + '</a></b>' + acc_string,\
                    parse_mode='html', disable_web_page_preview=True )

   #print(df1.groupby(ids[i]).count())
#   accs = df1.loc[df1['id_follow'] == ids[i]].inf_name
#   acc_string = ' and '
#   for acc in accs:
#    acc_string = acc_string  + acc + ", "
 
#   print("<b><a href='https://twitter.com/" + str(account) + "'>" + str(user_names[i]) + '</a></b>\n'\
#                    +  'created: '  + str(created[i]) + '\nfollowers: ' + str(followers[i]) + ' tweets: ' + str(tweets[i]) + '\n'\
#                    + str(decriptions[i]) \
#                    + "\n<b>followed by <a href='https://twitter.com/" + str(twi_ac_handle[user_couter]) + "'>"\
#                    + str(twi_ac_name[user_couter]) + '</a></b>' + acc_string)
            
   #print("<b><a href='https://twitter.com/" + str(twi_ac_handle[user_couter]) + "'>" + "" + str(twi_ac_name[user_couter]) + '</a></b>\n' + "<b><a href='https://twitter.com/" + str(account) + "'>" + str(user_names[i]) + '</a></b>\n'  +  'created: ' + str(created[i]) + '\n followers: ' + str(followers[i]) + ' tweets: ' + str(tweets[i]) + '\n' + str(decriptions[i]))
  
   i +=1
   for a in range(0,10):
    #print(i)    
    time.sleep(1)
    a +=1  

          