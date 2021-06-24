import praw
from settings import Settings

def main():
    settings = Settings('./settings.json')
    settings.parse_settings()
    
    reddit = praw.Reddit(
        client_id = settings.client_id,
        client_secret = settings.client_secret,
        password = settings.password,
        user_agent = settings.user_agent,
        username = settings.username,
    )
    print(reddit.user.me())

if __name__ == '__main__':
    main()