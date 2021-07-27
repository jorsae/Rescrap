import praw
import os, time, datetime
import logging
from peewee import *

from settings import Settings
from models import *
import constants

settings = Settings('../settings.json')

def login():
    reddit = praw.Reddit(
        client_id = settings.client_id,
        client_secret = settings.client_secret,
        password = settings.password,
        user_agent = settings.user_agent,
        username = settings.username,
    )
    return reddit
    for post in reddit.subreddit("csharp").hot(limit=1):
        print(post.title)
        print(post)
        print(post.selftext)
        print(post.url)

def setup_database():
    database.create_tables([PostModel])

def setup_logging():
    logFolder = '../logs'
    logFile = 'rescrap.log'
    if not os.path.isdir(logFolder):
        os.makedirs(logFolder)
    handler = logging.FileHandler(filename=f'{logFolder}/{logFile}', encoding='utf-8', mode='a+')
    logging.basicConfig(handlers=[handler], level=logging.INFO, format='%(asctime)s %(levelname)s:[%(filename)s:%(lineno)d] %(message)s')

def loop():
    while True:
        for subreddit in settings.subreddits:
            posts = None
            try:
                posts = reddit.subreddit(subreddit).new(limit=constants.NEW_POST_COUNT)
            except Exception as e:
                logging.error(e)
            
            for post in posts:
                post_exist = PostModel.select().where(PostModel.reddit_post_id == post)
                if post_exist.exists():
                    continue
                
                post_id, created = PostModel.get_or_create(reddit_post_id=post, subreddit=subreddit,
                                post_date=datetime.datetime.now(), author=post.author, title=post.title,
                                content=post.selftext, url=post.url)
                logging.info(f'[{subreddit}] Added post: {post}')
        time.sleep(settings.interval)

if __name__ == '__main__':
    setup_logging()
    settings.parse_settings()
    setup_database()

    reddit = login()
    logging.info(f'Logged in as: {reddit.user.me()}')
    loop()