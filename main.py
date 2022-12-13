from instabot import Bot
import json

credentials = json.load(open('credentials.json'))
username,password,targets = credentials["username"],credentials["password"],credentials["target"]


bot = Bot()

# Login to Instagram
bot.login(username=username, password=password)

for target in targets:

    followersIDs = bot.get_user_followers(target)

    for count,each_follower in enumerate(followersIDs):
        if count > 100:
            break
        bot.follow(each_follower) # Follow each follower

        sleep(1200) # Sleep for 15 seconds


        messasge_text = f'''Hello {bot.get_username_from_user_id(each_follower)}, do you need a person to outsource work to?

    Like copywriting, social media management, graphic design, video/reel editing, web development, funnel creation etc?

    Hi (username) , I'm Roy an engineering student looking for opportunities to assist you with my skills. Can we have a chat to see if we fit and compliment each other to grow?

    👉 Social media manager and growth
    👉 Content creation
    👉 Website/ App development
    👉 Graphic designers
    👉 Video editors
    👉 Virtual assistants'''
        bot.send_messages(messasge_text, [each_follower])

        print(f"message sent to {bot.get_username_from_user_id(each_follower)}")

bot.logout()