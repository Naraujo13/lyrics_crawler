import scrapy
import scrapy.crawler as crawler
import csv
class BandTracksSpider(scrapy.Spider):
  name = "tracks_spider"
  start_urls = []

  def __init__(self, start_url='', band_name='', **kwargs):
      self.start_urls = [start_url]
      self.band_name = band_name
      super().__init__(**kwargs)

  def parse(self, response):
    album_names = response.xpath(
      '//h3[@class="albumTitle"]//a/text()'
    ).getall()

    track_names = response.xpath('//a[@class="nameMusic"]/text()').getall()
    track_urls = list(map(
      lambda x: response.urljoin(x),
      response.xpath('//a[@class="nameMusic"]/@href').getall()
    ))

    self.write_results(track_names, track_urls)

  def write_results(self, names, urls):
    with open(f'data/{self.band_name}_tracks.tsv', 'w') as f:
      writer = csv.writer(f, delimiter='\t', lineterminator='\n')
      writer.writerows(zip(names, urls))
