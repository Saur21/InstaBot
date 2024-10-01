# # from instabot import Bot
# # bot = Bot() 
# # bot.login(username = "Insta id" , password = "#######")
# # # bot.follow("")
# # # bot.upload_phhoto("photo_adreess")
# # bot.unfollow("bddhwd4545")
from instabot import Bot

# Remove the cookie file before initializing the bot
import os# this is use to intracting with operating system
cookie_del =  'config/InstaId_uuid_and_cookie.json'  # This file might have a different name  UUID (Universally Unique Identifier),
if os.path.exists(cookie_del):
    os.remove(cookie_del)

bot = Bot()
bot.login(username="#####", password="#######")
# # bot.follow("InstaId")
# # bot.upload_phhoto("photo_adreess")
# bot.unfollow("instaId")
# bot.send_message("he",["Insta id" , "Another instaId"])
# followers = bot.get_user_followers("InstaId")
# for follower in followers:
#     print(bot.get_user_info(follower))
following = bot.get_user_followers("########")
for follow in following:
    print(bot.get_user_info(follow))

