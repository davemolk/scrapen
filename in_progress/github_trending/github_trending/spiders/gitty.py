from datetime import datetime

from github_trending.items import GithubTrendingItem
import scrapy
from scrapy.loader import ItemLoader


class GittySpider(scrapy.Spider):
    name = 'gitty'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/trending/']

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    }

    language_count = {}
    tally = 0

    def parse(self, response):
        repo_count = len(response.css('article.Box-row').getall())

        for repo in response.css("article.Box-row"):
            loader = ItemLoader(item = GithubTrendingItem(), selector=repo)
            loader.add_css("name", "h1.lh-condensed a::attr(href)")
            loader.add_css("link", "h1.lh-condensed a::attr(href)")
            loader.add_css("description", "h1.lh-condensed + p::text")
            loader.add_css("language", "span[itemprop='programmingLanguage']::text")
            loader.add_css("total_stars", "div.color-fg-muted a::text")
            loader.add_css("stars_today", "div.color-fg-muted span.float-sm-right::text")
            loader.add_value("date", datetime.now())
            
            repo_link = response.urljoin(repo.css('h1.lh-condensed a::attr(href)').get())
            
            yield scrapy.Request(
                repo_link,
                self.parse_details,
                cb_kwargs={
                    'loader': loader,
                    'repo_count': repo_count,
                },
            )

    def parse_details(self, response, loader, repo_count):
        self.tally += 1
        coders = response.css('div.Layout-sidebar ul.list-style-none li.mb-2.mr-2 a::attr(href)').getall()
        loader.add_value("contributors", coders)
            
        yield loader.load_item()

        # what are the popular languages for the day
        if loader.get_collected_values('language'):
            curr_lang = loader.get_collected_values('language')[0]
            self.language_count[curr_lang] = 1 + self.language_count.get(curr_lang, 0)
            if self.tally == repo_count:
                yield self.language_count