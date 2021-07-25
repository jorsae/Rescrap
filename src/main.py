import praw
import os, time
import logging
from settings import Settings

settings = Settings('./settings.json')

def login():
    reddit = praw.Reddit(
        client_id = settings.client_id,
        client_secret = settings.client_secret,
        password = settings.password,
        user_agent = settings.user_agent,
        username = settings.username,
    )
    return reddit
    for submission in reddit.subreddit("csharp").hot(limit=1):
        print(submission.title)
        print(submission)
        print(submission.selftext)
        print(submission.url)

def setup_logging():
    logFolder = 'logs'
    logFile = 'rescrap.log'
    if not os.path.isdir(logFolder):
        os.makedirs(logFolder)
    handler = logging.FileHandler(filename=f'{logFolder}/{logFile}', encoding='utf-8', mode='a+')
    logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s %(levelname)s:[%(filename)s:%(lineno)d] %(message)s')

def loop():
    time.sleep(settings.interval)

if __name__ == '__main__':
    setup_logging()
    settings.parse_settings()

    reddit = login()
    logging.info(f'Logged in as: {reddit.user.me()}')
    loop()