from peewee import *
from models import BaseModel

class PostModel(BaseModel):
    post_id = AutoField()
    reddit_post_id = TextField()
    subreddit = TextField()
    post_date = DateTimeField()
    author = TextField()
    title = TextField()
    content = TextField()
    url = TextField()

    class Meta:
        table_name = 'Posts'