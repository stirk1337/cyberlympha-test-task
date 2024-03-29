from fastapi import Depends
from pydantic import parse_obj_as

from repository.news_repository import NewsRepository
from schemas.news import NewsList, NewsWithComments


class NewsService:
    def __init__(self, news_repository: NewsRepository = Depends()):
        self.news_repository = news_repository

    def get_all_news(self) -> NewsList:
        news = self.news_repository.get_all_news()
        return parse_obj_as(NewsList, news)

    def get_news_by_id(self, news_id: int) -> dict | None:
        return self.news_repository.get_news_by_id(news_id)

    def get_news_with_comments(self, news_id: int) -> NewsWithComments | None:
        news = self.news_repository.get_news_by_id(news_id)
        if not news:
            return None

        news["comments"] = self.news_repository.get_comments_for_news(news_id)
        return parse_obj_as(NewsWithComments, news)
