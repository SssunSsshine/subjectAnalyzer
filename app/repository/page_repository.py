import logging
from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from app import db
from app.models.page import Page


class PageRepository:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add_page(self, page):
        try:
            with db.session.begin():
                db.session.add(page)
        except IntegrityError:
            db.session.rollback()
            self.logger.error(f"Страница с URL {page.url} уже существует")
            self.update_page(page)
        except SQLAlchemyError as e:
            db.session.rollback()
            self.logger.error(f"Ошибка добавления страницы с URL {page.url}: ", e)

    def add_pages(self, pages):
        for page in pages:
            self.add_page(page)

    def get_page_by_url(self, url):
        try:
            with db.session.begin():
                page = db.session.query(Page).filter_by(url=url).first()
        except SQLAlchemyError as e:
            db.session.rollback()
            self.logger.error(f"Ошибка получения страницы с URL {page.url}: ", e)
            return None

        return page

    def update_page(self, page):
        try:
            updated_page = db.session.query(Page).filter_by(url=page.url).first()
            if updated_page:
                updated_page.content = page.content
                updated_page.crawled_at = datetime.now()
                db.session.commit()
                print(f"Страница с URL {updated_page.url} успешно обновлена")
        except SQLAlchemyError as e:
            db.session.rollback()
            self.logger.error(f"Ошибка обновления страницы с {page.url}: ", e)
