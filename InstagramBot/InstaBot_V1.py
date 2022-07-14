#Libraries to scrape Instagram Data
from instabot import Bot
from instascrape import Hashtag 


#Establishing a user promotion class
# class user_promotion():

#Instagram promotion function, inside the userpromotion class
def instagram_scraper():
    #Extablish the bot
    bot = Bot()
    
    #Have the bot login to the instagram account
    bot.login(username = "", password = "Kksiga123$")

    #Input the Account we are promiting, and the main topic of the account
    account_Topic = input()
    promotername = input()
    
    #Create list to track what accounts have already been sent a messgae
    list_accounts = []

    #Get the accounts using the hashtags relating to the customers topic
    accounts = bot.get_hashtag_users(str(account_Topic))


    #Loop through sending the folowers of the accounts using these hashtags, and the accounts using the hashtag, then send a promotional message
    for account in accounts:
        #If the account has not already been sent a message, it will send the account, and its followers a message
        if account not in list_accounts:
            list_accounts.append(account)
            bot.send_message("Hello! We have seen your intrest in " + str(account_Topic) + ", and recomend this " + str(promotername) + ". Go check them out!", [str(account)])
            followers = bot.get_user_followers(account)
            for follower in followers:
                follower_info = bot.get_user_info(follower)
                user_name = follower_info['full_name']
                bot.send_message("Hello" + str(user_name) + "! We have seen your intrest in " + str(account_Topic) + ", and recomend this " + str(promotername) + ". Go check them out!", [str(follower)])
                bot.delay(5)



def reddit_promotion():
    placeholder = 1

def facebook_promotion():
    placeholder = 1


#Call the class
# user_promotion()

#Alternate way to scarpe the users of a hashtag if the other one doesn't work
# google_hashtag = Hashtag('google')
# google_hashtag.scrape()
# google_hashtag.to_dict()



instagram_scraper()