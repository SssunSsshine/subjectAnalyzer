import logging
from urllib.parse import urljoin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from app.crawlers.chrome_driver_manager import ChromeDriverManager


class RbcCrawler:
    def __init__(self, driver_manager):
        self.driver_manager = driver_manager
        self.logger = logging.getLogger(__name__)

    def get_html(self, url):
        if self.driver_manager.driver is None:
            raise Exception("Драйвер не запущен. Вызовите метод start() перед использованием get_html().")

        self.driver_manager.driver.get(url)
        self.driver_manager.driver.implicitly_wait(5)
        return self.driver_manager.driver.page_source

    def crawl(self, url):
        has_next_page = 0
        all_links = []
        while has_next_page < 2:
            self.driver_manager.driver.get(url)
            self.driver_manager.driver.implicitly_wait(5)
            # Собираем ссылки внутри docListContainer
            try:
                self.get_judgment_inks(all_links, url)
            except Exception as e:
                self.logger.error('Ошибка поиска docListContainer или ссылок', e)

            # Ищем ссылку на следующую страницу
            try:
                has_next_page, url = self.get_next_page_link(has_next_page, url)
            except Exception as e:
                self.logger.error('Следующая страница не найдена', e)
                has_next_page = 2
        return all_links

    def get_next_page_link(self, has_next_page, url):
        next_page_element = self.driver_manager.driver.find_element(By.XPATH,
                                                                    '//div[@class="h-pager-wrap"]//span['
                                                                    '@class="page-next"]/a')
        if next_page_element:
            next_page_url = next_page_element.get_attribute('href')
            if next_page_url:
                url = urljoin(url, next_page_url)
                self.logger.info(f'Переходим на следующую страницу: {url}')
                has_next_page += 1
            else:
                has_next_page = 2
        else:
            has_next_page = 2
        return has_next_page, url

    def get_judgment_inks(self, all_links, url):
        doc_list_container = WebDriverWait(self.driver_manager.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'docListContainer'))
        )
        links = doc_list_container.find_elements(By.XPATH, './/a[not(ancestor::div[contains(@class,'
                                                           '"h-pager-wrap")])]')
        if links:
            for link in links:
                href = link.get_attribute('href')
                if href:
                    full_url = urljoin(url, href)
                    all_links.append(full_url)
                    print(f'Найдена ссылка: {full_url}')
        else:
            self.logger.warning("Не найдены ссылки в docListContainer.")


if __name__ == "__main__":
    driver_manager = ChromeDriverManager()
    driver_manager.start()

    crawler = SudactCrawler(driver_manager)
    start_url = ('https://sudact.ru/regular/doc/?regular-txt=гусев&regular-case_doc=&regular-lawchunkinfo=&regular'
                 '-date_from=&regular-date_to=&regular-workflow_stage=&regular-area=&regular-court=&regular-judge'
                 '=#searchResult')
    all_links = crawler.crawl(start_url)

    print("Found links:")
    for link in all_links:
        print(link)

    driver_manager.stop()
