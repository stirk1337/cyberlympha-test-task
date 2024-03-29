from typing import List


import json


class NewsRepository:
    def __init__(self):
        self.news_file_path = "src/repository/json/news.json"
        self.comments_file_path = "src/repository/json/comments.json"

    def get_not_deleted_news(self) -> dict:
        with open(self.news_file_path, "r") as news_file:
            news_data = json.load(news_file)
        news_data["news"] = [
            news for news in news_data["news"] if not news.get("deleted", False)
        ]
        return news_data

    def get_comments_for_news(self, news_id: int) -> List[dict]:
        with open(self.comments_file_path, "r") as comments_file:
            comments_data = json.load(comments_file)
        return [
            comment
            for comment in comments_data["comments"]
            if comment["news_id"] == news_id
        ]

    def get_news_by_id(self, news_id: int) -> dict | None:
        news_list = self.get_not_deleted_news()["news"]
        for news_item in news_list:
            if news_item["id"] == news_id:
                return news_item
        return None
