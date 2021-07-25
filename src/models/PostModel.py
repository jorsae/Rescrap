from peewee import *
from models import BaseModel

class PostModel(BaseModel):
    post_id = AutoField()
    post_date = DateField()
    author = TextField()
    title = TextField()
    content = TextField()

    class Meta:
        table_name = 'Posts'