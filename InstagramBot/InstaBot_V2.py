#Libraries, and API's used
#INSTAPY :: INSTAPY = Used to get the usernames
#INSTADM :: INSTADM =  used to send messages, (DM's)) to the users
#TIME :: SLEEP = Used to set a break period for the bot
from time import sleep
from instapy import InstaPy
from instadm import InstaDM

# Global instance of login credentials
global insta_username
global insta_password

#Enter in the username, and password to login
insta_username = '1112'
insta_password = '1112'


#Create a function to message the users on instagram
def message_User():
    
    #Define messages sent, and set it equal to 0
    messages_sent = 0

    #Run the sendd message function untile their is no more users to send a message to
    while(len(hashtag_USERS) > 0):
        
        #Send 150 messages every 15 minutes, to avoid suspision
        if messages_sent < 150:
            #Iterate through the users, and send each of them a message
            for user_ in hashtag_USERS:
                #Run InstaDm API on Headless browser to send message to the users
                instabots = InstaDM(username= str(insta_username), password= str(insta_password), headless = True)

                #Send the message to the users using the InstaDM API
                instabots.sendMessage(user = str(user_) , message = '')

                #Remove the user from the list so, the next user can be senta message
                hashtag_USERS.remove(user_)
                
                #Stop the function for 10 seconds to stop some suspicious activity
                sleep(10)
                messages_sent += 1
        
        #If 150 messages are sent, tghen set the sent_messages to 0 to rest, and set the function to sleep for 15 minutes, then restart, until all the users have been sent a message
        else:
            #Reset message sent to 0
            messages_sent = 0
            #Sett it to sleep for 15 minutes
            sleep(15*60)

#Get the users username using the InstaPY API 
# Input the set amount you want the program to run in MINUTES
def Instagram_Scraper(set_runtime):
    
    #_____VARIABLES______
    setruntime = int(set_runtime)

    #Input the Account we are promiting, and the main topic of the account
    account_Topic = ""
    promotername = ""

    #Create a list to hold the usernames, of the users already sent a message
    user_list = []

    #Establish the global instance of the runtime variable setting it to a default of 0
    runtime = 0
    
    #Declare a global instance of the HAshtag users list to use in the sen message list
    global hashtag_USERS
    hashtag_USERS = []


    #____ESTABLISHING THE SESSION_____

    #Get into a instagram session by loging in with the username and password provided above, and run int he backround, with headless chrome
    session = InstaPy(username=insta_username,password=insta_password, headless_browser = True)

    # Settings to only target high profile acounts, and avoid bots(CAN REMOVE IF WANTED)
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True,min_followers= 10000,min_following=10)

    #To start a selenium remote session (NOT NEEDED)
    # session.set_selenium_remote_session()



    #______THE ACTUAL SCRAPER_____

    #Loop until the set run time is reached
    while((runtime/60) < setruntime):
        
        #Delay the program by 10 seconds,. to stop any suspicious activity notificaitions, and give the computer some rest time, by sleeping for 10 seconds after unfollowing
        session.set_action_delays(enabled = True, follow = 5)

        #Follow a user of a hashtag
        session.follow_by_tags(['tag1', 'tag2'], amount= 10000)

        #Get the users username
        account = session.grab_following(username = str(insta_username))

        for account_ in account:
            
            if account_ not in user_list:    
            
                #Add the name of the user who is being sent the message, to the user_list, to keep track of what users have already been sent a message
                user_list.append(account_)

                #Get the followers of the account
                followers_account = session.grab_following(username = str(account))

                #Append the users to a list to be used by the send message function
                hashtag_USERS.append(followers_account)
                hashtag_USERS.append(account_)

                #Comment on all the posts of the peron, so other people can see the link, and follow
                session.set_do_comment(enabled = True, percentage = 100)
                session.set_comments("Hello! We have seen your intrest in " + str(account_Topic) + ", and recomend this " + str(promotername) + ". Go check them out!")
                
                # _____NEED TO IMPLEMENT A RANDOM PERCENTAGE CHANCE THE BOT WILL REPLY TO THE COMMENTORS ON THE POSTS WITH THE PROMOTIONAL MESSAGE. ALSO A SET NUMBER OF COMMENTS PER POST_____

                #Delay the program by 5 seconds,. to stop any suspicious activity notificaitions, and give the computer some rest time, by sleeping for 10 seconds after unfollowing
                session.set_action_delays(enabled = True, unfollow = 5)

                #Unfollow a user of a hashtag
                session.unfollow_users(amount = 1)

                #Adds a value of 10 seconds to run time
                runtime += 10

            else:
                #Unfollow a user of a hashtag ___NEED TO FIX TO UNFOLLOW (ACCOUNT_)
                session.unfollow_users(amount = 1)
    
    #Logous out of the instagram account, so the InstaDM API can login and start messaging
    session.end()

    #Stalls 5 minutes before loging in for another session to message the users
    sleep(5*60)

    #Call the message user function
    message_User()


#Call the Instagram Scraper function with the parameter of a set runtime (60 MINUTES)
Instagram_Scraper(60)




"""

____TODO LIST_____
1. Getrid of the runtime, and set it to follow a set number of people (AKA, 10,000)
2. NEED TO IMPLEMENT A RANDOM PERCENTAGE CHANCE THE BOT WILL REPLY TO THE COMMENTORS 
   ON THE POSTS WITH THE PROMOTIONAL MESSAGE. ALSO A SET NUMBER OF COMMENTS PER POST
3. TEST

"""
