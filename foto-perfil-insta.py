import instaloader

bot = instaloader.Instaloader()

username = "reis__011"

print(bot.download_title_pic(username, profile_pic_only=True))