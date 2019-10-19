# scrapy runspider lyrics_spider.py -o data/lyrics.json -t json
import scrapy
import scrapy.crawler as crawler
import csv
from scrapy.http import Request
class LyricsSpider(scrapy.Spider):
  name = "lyrics_spider"
  start_urls = []

  def __init__(self,  band_name='', **kwargs):
      self.band_name = band_name
      super().__init__(**kwargs)

  def start_requests(self):
    with open(f'data/{self.band_name}_tracks.tsv') as f:
      reader = csv.reader(f, delimiter='\t')
      for line in reader:
        yield Request(line[1])

  def parse(self, response):
    track_name = response.xpath(
      '//div[@id="lyricContent"]//div//h1/text()'
    ).get()

    album_name = response.xpath(
      '//div[@id="lyricContent"]//div//h3//a//small/text()'
    ).get()

    lyrics = '\n'.join(response.xpath('//div[@id="lyrics"]/text()').getall())

    return {
      'album_name': album_name,
      'track_name': track_name,
      'corpus': lyrics
    }



