from instabot import Bot

def main():
    # Create an instance of the Bot
    bot = Bot()

    # Login to your Instagram account
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")
    bot.login(username=username, password=password)

    # Follow users based on a hashtag
    hashtag = input("Enter a hashtag to search for (without #): ")
    num_users = int(input("Enter the number of users to follow: "))

    # Follow users who have posted under the specified hashtag
    bot.follow_users(bot.get_hashtag_users(hashtag)[:num_users])

    print(f"Followed {num_users} users who posted with #{hashtag}.")

if __name__ == "__main__":
    main()
