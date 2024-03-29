from fastapi import APIRouter, HTTPException, Depends

from schemas.news import NewsWithComments, NewsList
from services.news_service import NewsService

router = APIRouter()


@router.get("/", response_model=NewsList)
async def get_all_news(news_service: NewsService = Depends()):
    """
    Returns list of all news along with the news count.
    """
    return news_service.get_all_news()


@router.get(
    "/news/{news_id}",
    response_model=NewsWithComments,
    responses={404: {"description": "News not found"}},
)
async def get_news_by_id(news_id: int, news_service: NewsService = Depends()):
    """
    Returns specific news along with its comments, if any.
    """
    news = news_service.get_news_with_comments(news_id)
    if news:
        return news
    else:
        raise HTTPException(status_code=404, detail="News not found")
