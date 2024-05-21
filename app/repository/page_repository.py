import logging
from sqlalchemy.exc import SQLAlchemyError

from app import db
from app.models.page import Page


class PageRepository:

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def add_page(self, page):
        try:
            with db.session.begin():
                db.session.add(page)
        except SQLAlchemyError as e:
            db.session.rollback()
            self.logger.error(f"Error adding page with URL {page.url}: ", e)

    def add_pages(self, pages):
        for page in pages:
            self.add_page(page)

    def get_page_by_url(self, url):
        try:
            with db.session.begin():
                page = db.session.query(Page).filter_by(url=url).first()
        except SQLAlchemyError as e:
            db.session.rollback()
            return None

        return page
