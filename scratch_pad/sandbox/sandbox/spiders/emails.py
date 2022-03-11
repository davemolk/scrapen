import scrapy

import re

class GetEmail(scrapy.Spider):
    name = 'e'

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Safari/537.36',
        }

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_domains = [f'{url}']
        self.start_urls = [f'https://{url}']
        self.ignored_extensions = ['.aif','.cda','.mid','.midi','.mp3','.mpa','.ogg','.wav','.wma','.wpl','.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip','.bin','.dmg','.iso','.toast','.vcd','.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.apk','.bat','.bin','.cgi','.pl','.exe','.gadget','.jar','.py','.wsf','.fnt','.fon','.otf','.ttf','.ai','.bmp','.gif','.ico','.jpeg','.jpg','.png','.ps','.psd','.svg','.tif','.tiff','.asp','.cer','.cfm','.cgi','.pl','.part','.py','.rss','.key','.odp','.pps','.ppt','.pptx','.c','.class','.cpp','.cs','.h','.java','.sh','.swift','.vb','.ods','.xlr','.xls','.xlsx','.bak','.cab','.cfg','.cpl','.cur','.dll','.dmp','.drv','.icns','.ico','.ini','.lnk','.msi','.sys','.tmp','.3g2','.3gp','.avi','.flv','.h264','.m4v','.mkv','.mov','.mp4','.mpg','.mpeg','.rm','.swf','.vob','.wmv','.doc','.docx','.odt','.pdf','.rtf','.tex','.txt','.wks','.wps','.wpd']
        self.total_emails = 0

    def parse(self, response):
        for link in response.css('a::attr(href)'):
            link = response.urljoin(link.get())
            yield scrapy.Request(link,
                                self.parse_details)

    def parse_details(self, response):
        emails = re.findall(r"[\w.+-]@[\w-]+\.[\w.-]+", response.text)
        for e in emails:
            self.total_emails += 1
            print('email total: ', self.total_emails)
            yield {
                'url': response.url,
                'email': e
            }
        
        # need to parse each page for links to follow as well, so maybe using crawlspider as a base model would be better
        # tweak above regex and handle name [at] domain and similar instances
        # use an item for storage