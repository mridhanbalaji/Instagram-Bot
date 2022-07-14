from instabot import Bot



#Extablish the bot
bot = Bot()

#Have the bot login to the instagram account
bot.login(username = "mridhbala_21", password = "mridhbala1234$")

#Input the Account we are promiting, and the main topic of the account
account_Topic = "Cooking"
promotername = "Raj"


test = 0
accounts = list()

while test > 2:
    accounts = bot.get_hashtag_users(str(account_Topic))
    test += 1

print(accounts)

#Loop through sending the folowers of the accounts using these hashtags, and the accounts using the hashtag, then send a promotional message
# for account in accounts:
#     bot.send_message("Hello! We have seen your intrest in " + str(account_Topic) + ", and recomend this " + str(promotername) + ". Go check them out!", [str(account)])
#     followers = bot.get_user_followers(str(account))
#     for follower in followers:
#         bot.send_message("Hello! We have seen your intrest in " + str(account_Topic) + ", and recomend this " + str(promotername) + ". Go check them out!", [str(follower)])
#         bot.delay(5)