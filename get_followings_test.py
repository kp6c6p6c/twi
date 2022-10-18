import tweepy
import regex
import array 
import os
from datetime import datetime, timedelta
from itertools import islice
import pandas as pd
import time
import sys
import dateutil.parser

#client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAOYsgQEAAAAANfaQ1N%2Bi0zF%2Ba0oDPtKqVJBILuw%3D0spLNSTHo0YQwFRybKMgz51KBNyf82J2I5S486R2w0wuouiYS1")
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAABp%2FiAEAAAAAQcJ9njpzHjekMm1q1nILjZAa5f0%3DKyrlcMygeXpox1V4a919sjRGmAesPXCMkUguXr8OlsfSnyTHZL")
WAT_IS_EARLY = 200
DATA_FOLDER = "./data/"
CONF_FOLDER = "./"

def remove_control_characters(str):
    return regex.sub(r'\p{C}', '', str)


today_date = str(datetime.today().date())
yesterday_date = str(datetime.today().date() - timedelta(days=1))
#twitter_acs  = pd.read_csv('twitter_acc', sep = '\t')



def write_new_followings(infl_id, infl_handle, infl_name, max_res = 10): 
 data=[]
 line=[]
 filename = str(infl_id) + "_" + today_date + '.csv' 
 response = client.get_users_following(infl_id, max_results=max_res, user_fields=["id", "name","description","created_at", "public_metrics"]) 
 for acc in response.data:
  desc = remove_control_characters(acc.description)
  date_created = dateutil.parser.isoparse(str(acc.created_at)).date()
  user_count = int(acc.public_metrics['followers_count'])
  if user_count < WAT_IS_EARLY:
   line = [today_date, infl_id, infl_handle, infl_name, acc.id, acc.username, acc.name, desc, date_created, acc.public_metrics['followers_count'], acc.public_metrics['tweet_count']]
   data.append(line)
 df = pd.DataFrame(data)
 df.to_csv(DATA_FOLDER + filename, header=False, sep='\t', index=False, mode='w')
 return


#res = write_new_followings(205123298, 1)


if len (sys.argv) > 1:
 twi_ac_filename = sys.argv[1]
else:
 print ("дай оргументов!")

df = pd.read_csv(CONF_FOLDER + twi_ac_filename, sep = '\t')
infl_ids = df['id'].tolist()
infl_handles = df['handle'].tolist()
infl_names = df['name'].tolist()
i=0

for infl_id in infl_ids:
 print(infl_names[i])
 res = write_new_followings(infl_id, infl_handles[i], infl_names[i], 10)
 #for a in range(0,10):
   #print(i)
   # making delay for 1 second
  # time.sleep(1)
 i +=1

