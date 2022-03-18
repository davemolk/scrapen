from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader
from github_trending.items import GithubTrendingItem


class GittySpider(scrapy.Spider):
    name = 'gitty'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/trending/']

    # custom_settings = {
    #     'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
    # }

    def parse(self, response):
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
                cb_kwargs={'loader': loader}
            )

    def parse_details(self, response, loader):
            coders = response.css('div.Layout-sidebar ul.list-style-none li.mb-2.mr-2 a::attr(href)').getall()
            loader.add_value("contributors", coders)
            yield loader.load_item()