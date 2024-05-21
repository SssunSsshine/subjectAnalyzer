from datetime import datetime
import logging

from app.models.page import Page
from app.repository.page_repository import PageRepository


class PageService:
    def __init__(self):
        self.page_repository = PageRepository()
        self.logger = logging.getLogger(__name__)

    def add_page(self, content, current_time, url):
        page = Page(
            url=url,
            content=content,
            crawled_at=current_time
        )

        try:
            self.page_repository.add_page(page)
            self.logger.info(f"Страница с URL {page.url} успешно добавлена")
            return True
        except Exception as e:
            self.logger.error('Ошибка добавления страницы', e)
            return False

    def add_pages(self, url_content_map):
        if not url_content_map:
            return False
        try:
            pages = []
            for url, content in url_content_map.items():
                page = Page(
                    url=url,
                    content=content,
                    crawled_at=datetime.now()
                )
                pages.append(page)

            if not pages:
                self.logger.warning("Список страниц пуст")
                return False

            self.page_repository.add_pages(pages)
            self.logger.info("Страницы успешно добавлены")
            return True
        except Exception as e:
            self.logger.error('Ошибка добавления страниц', e)
            return False

    def get_page_by_url(self, url):
        try:
            page = self.page_repository.get_page_by_url(url)
            if page is None:
                self.logger.warning(f'Страница с URL {url} не найдена')
            return page
        except Exception as e:
            self.logger.error('Ошибка при поиске страницы по URL', e)
