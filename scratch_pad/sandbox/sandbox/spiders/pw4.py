from curses import meta
from pathlib import Path

from scrapy import Spider, FormRequest
from scrapy_playwright.page import PageCoroutine


class Posty(Spider):
    name = 'posty'

    def start_requests(self):
        yield FormRequest(
            url='https://httpbin.org/forms/post',
            formdata={"foo": "bar"},
            meta={
                "playwright": True,
                "playwright_page_coroutines": [
                    PageCoroutine(
                        "screenshot", path=Path(__file__).parent / "post.png", full_page=True
                    ),
                ],
            },
        )

    def parse(self, response):
        yield {'url': response.url}