from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Link(CrawlSpider):
    name = 'l'

    ignored_extensions = ['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl','.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip','.bin','.dmg','.iso','.toast','.vcd','.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.apk','.bat','.bin','.cgi','.pl','.exe','.gadget','.jar','.py','.wsf','.fnt','.fon','.otf','.ttf','.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff','.asp','.cer','.cfm','.cgi','.pl','.part','.py','.rss','.key','.odp','.pps','.ppt','.pptx','.c','.class','.cpp','.cs','.h','.java','.sh','.swift','.vb','.ods','.xlr','.xls','.xlsx','.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp','.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wks','.wps','.wpd']


    rules = (
        Rule(LinkExtractor(allow=()), 
                callback="parse_item", 
                follow=True),

        Rule(LinkExtractor(deny_extensions=ignored_extensions)),
    )

    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']

    def parse_item(self, response):
        # self.logger.info('landed on %s', response.url)
        print()
        yield {
            "title": response.css('title::text').get(),
            'url': response.url
        }