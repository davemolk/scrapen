from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader
from github_trending.items import GithubTrendingItem


class GittySpider(scrapy.Spider):
    name = 'gitty'
    allowed_domains = ['github.com/trending']
    start_urls = ['http://github.com/trending/']

    def parse(self, response):
        for repo in response.css("article.Box-row"):
            l = ItemLoader(item = GithubTrendingItem(), selector=repo)
            l.add_css("name", "h1.lh-condensed a::attr(href)")
            l.add_css("link", "h1.lh-condensed a::attr(href)")
            l.add_css("desc", "h1.lh-condensed + p::text")
            l.add_css("language", "span[itemprop='programmingLanguage']::text")
            l.add_css("total_stars", "div.color-fg-muted a::text")
            l.add_css("stars_today", "div.color-fg-muted span.float-sm-right::text")
            l.add_value("date", datetime.now()) # come back to this

            yield l.load_item()


            # scraped_link = repo.css("h1.lh-condensed a::attr(href)").get()
            # yield {
            #     'name': scraped_link,
            #     'link': urllib.parse.urljoin(response.url, scraped_link),
            #     'desc': repo.css("h1.lh-condensed + p::text").get().strip(),
            #     'language': repo.css("span[itemprop='programmingLanguage']::text").get(),
            #     # 'total_stars': repo.css("div.color-fg-muted a::text").get().strip(),
            #     # 'stars_today': repo.css("div.color-fg-muted span.float-sm-right::text").get(),
            # }
            
            # need some error handling for missing values


    # def parse(self, response):
    #     for repo in response.css("article.Box-row"):
    #         l = ItemLoader(item = GithubTrendingItem(), selector=repo)
    #         scraped_link = repo.css("h1.lh-condensed a::attr(href)").get()
    #         yield {
    #             'name': scraped_link,
    #             'link': urllib.parse.urljoin(response.url, scraped_link),
    #             'desc': repo.css("h1.lh-condensed + p::text").get().strip(),
    #             'language': repo.css("span[itemprop='programmingLanguage']::text").get(),
    #             # 'total_stars': repo.css("div.color-fg-muted a::text").get().strip(),
    #             # 'stars_today': repo.css("div.color-fg-muted span.float-sm-right::text").get(),
    #         }
            
            # need some error handling for missing values