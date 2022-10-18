import tweepy
import regex
import array 
import os
from datetime import datetime, timedelta
from itertools import islice
import pandas as pd
client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAOYsgQEAAAAANfaQ1N%2Bi0zF%2Ba0oDPtKqVJBILuw%3D0spLNSTHo0YQwFRybKMgz51KBNyf82J2I5S486R2w0wuouiYS1")
client2 = tweepy.Client("AAAAAAAAAAAAAAAAAAAAABp%2FiAEAAAAAQcJ9njpzHjekMm1q1nILjZAa5f0%3DKyrlcMygeXpox1V4a919sjRGmAesPXCMkUguXr8OlsfSnyTHZL")


def remove_control_characters(str):
    return regex.sub(r'\p{C}', '', str)


today = str(datetime.today().date())
yesterday = str(datetime.today().date() - timedelta(days=1))


def write_new_followings(user_id, max_res = 20): 
    response = client.get_users_following(user_id, max_results=max_res, user_fields=["id", "description"])
    file = open(str(user_id) + "_" + today + '.csv', 'w')
    for user in response.data:
      desc = remove_control_characters(user.description)
      file.write(str(user.id) + '\t@' +  user.username + '\t' + desc + '\n')
      data.append(str(user.id) + '\t@' +  user.username + '\t' + desc + '\n')
    file.close()
    return
    


for user_id in user_ids:
    data = []
    res = write_new_followings(user_id, 20)
    i = 1
    for filename in os.listdir('.'):
       prev_day_file = str(user_id) + "_" + str(datetime.today().date() - timedelta(days= i )) + '.csv'
       i = i + 1
       if filename == prev_day_file:
         print(filename)
         break
    try:
         file1 = open(prev_day_file,'r')
    except IOError as e:
      print("skip")
    else:
      with file1:
        file_all_acc = open("new_following.csv",'a')
        same = set(data) - set(file1)
        same.discard('\n')
        file1.close()
        file2 = open(str(user_id) + "_NEW_" + today + '.csv', 'w')
        for line in same:
             file2.write(line)
             file_all_acc.write(today + '\t' + str(user_id) + "\t" + line)
        file2.close()
        file_all_acc.close()

