import tweepy
import regex
import array 
from datetime import datetime, timedelta
from itertools import islice

client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAAOYsgQEAAAAANfaQ1N%2Bi0zF%2Ba0oDPtKqVJBILuw%3D0spLNSTHo0YQwFRybKMgz51KBNyf82J2I5S486R2w0wuouiYS1")


# Get Users

# This endpoint/method returns a variety of information about one or more users
# specified by the requested IDs or usernames


list_ids=[1550097188583313408, 1567874364124631045, 1566909054420647938]


# By default, only the ID, name, and username fields of each user will be
# returned
# Additional fields can be retrieved using the user_fields parameter

def remove_control_characters(str):
    return regex.sub(r'\p{C}', '', str)


today = str(datetime.today().date())
yesterday = str(datetime.today().date() - timedelta(days=1))

for list_id in list_ids:
    data = []
    response = client.get_list_members(list_id, max_results = 20, user_fields=["id", "description"])
    file = open("list-" + str(list_id) + "_" + today + '.csv', 'w')
    for user in response.data:
      desc = remove_control_characters(user.description)
      file.write(str(user.id) + '\t@' +  user.username + '\t' + desc + '\n')
      data.append(str(user.id) + '\t@' +  user.username + '\t' + desc  + '\n')

    file.close()
    try:
         file1 = open("list-" + str(list_id) + "_" + yesterday + '.csv','r')
    except IOError as e:
      print("skip")
    else:
      with file1:
        file_all_acc = open("list-new.csv",'a')
        same = set(data) - set(file1)
        same.discard('\n')
        file1.close()
        file2 = open("list-" + str(list_id) + "_NEW_" + today + '.csv', 'w')
        for line in same:
             file2.write(line)
             file_all_acc.write(today + '\t' + str(list_id) + "\t" + line)
        file2.close()
        file_all_acc.close()




# By default, this endpoint/method returns 100 results
# You can retrieve up to 1000 users by specifying max_results
#response = client.get_users_followers(user_id, max_results=1000)


#with open('1', 'r') as file1:
# with open('2', 'r') as file2:
#   same = set(file2) - set(file1)
#   same.discard('\n')
# for line in same:
#  print(line)


#for user_id in user_ids:
#    data = []
#    response = client.get_users_following(user_id, max_results = 10, user_fields=["id", "description", "url"]) 
#    file1 = open(str(user_id), 'r')
#    print(str(user_id) + "--------------------------\n")
#    for user in response.data:
#      desc = remove_control_characters(user.description)
#      data.append(str(user.id) + ' @' +  user.username + ' ' + desc + ' ' + user.url + '\n')
#    same = set(data) - set(file1)
#    same.discard('\n')
#    file1.close()
#    for line in same:
#       print(line)



