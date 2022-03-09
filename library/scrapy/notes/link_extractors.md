Link extractors are used in CrawlSpider spiders through a set of Rule objects. You can also use link extractors in regular spiders. For example, you can instantiate LinkExtractor into a class variable in your spider, and use it from your spider callbacks:

def parse(self, response):
    for link in self.link_extractor.extract_links(response):
        yield Request(link.url, callback=self.parse)


# parameters (a few of many)
allow (str or list) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be extracted. If not given (or empty), it will match all links.

deny (str or list) – a single regular expression (or list of regular expressions) that the (absolute) urls must match in order to be excluded (i.e. not extracted). It has precedence over the allow parameter. If not given (or empty) it won’t exclude any links.

restrict_css (str or list) – a CSS selector (or list of selectors) which defines regions inside the response where links should be extracted from. Has the same behaviour as restrict_xpaths.

restrict_text (str or list) – a single regular expression (or list of regular expressions) that the link’s text must match in order to be extracted. If not given (or empty), it will match all links. If a list of regular expressions is given, the link will be extracted if it matches at least one.

unique (bool) – whether duplicate filtering should be applied to extracted links.

strip (bool) – whether to strip whitespaces from extracted attributes. According to HTML5 standard, leading and trailing whitespaces must be stripped from href attributes of <a>, <area> and many other elements, src attribute of <img>, <iframe> elements, etc., so LinkExtractor strips space chars by default.


# extract_links(response)[source]¶
Returns a list of Link objects from the specified response.

Only links that match the settings passed to the __init__ method of the link extractor are returned and duplicate links are omitted.