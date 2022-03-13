import scrapy
from scrapy_playwright.page import PageCoroutine

class ClickAndSavePdfSpider(scrapy.Spider):
    name = "pdf"

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.org",
            meta=dict(
                playwright=True,
                playwright_page_coroutines={
                    "click": PageCoroutine("click", selector="a"),
                    "pdf": PageCoroutine("pdf", path="/tmp/file.pdf"),
                },
            ),
        )

    def parse(self, response):
        pdf_bytes = response.meta["playwright_page_coroutines"]["pdf"].result
        with open("iana.pdf", "wb") as fp:
            fp.write(pdf_bytes)
        yield {"url": response.url}  # response.url is "https://www.iana.org/domains/reserved"