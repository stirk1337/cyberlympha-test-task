from pydantic import BaseModel
from typing import List


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: str
    comment: str


class News(BaseModel):
    id: int
    title: str
    date: str
    body: str
    deleted: bool
    comments_count: int


class NewsList(BaseModel):
    news: List[News]
    news_count: int


class NewsWithComments(News):
    comments: List[Comment]
