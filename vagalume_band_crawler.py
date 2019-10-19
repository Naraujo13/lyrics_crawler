import os
import sys

if len(sys.argv) < 2:
  print(
    'Script necessita da url da página inicial da banda como argumento' +
    '\nUso: python vagalume_band_crawler.py url_da_banda'
  )
  exit(1)

if not os.path.exists('data/'):
  os.mkdir('data/')


band_home_page = sys.argv[1]
if 'discografia/' not in band_home_page:
  band_home_page += 'discografia/'


band_name = band_home_page.replace('http://', '').replace('https://', '')
band_name = band_name.replace('www.', '').replace('vagalume.com.br/', '')
band_name = band_name.replace('/discografia', '').replace('/', '').replace('-', '_').replace('\\', '_')

command_1 = f'scrapy crawl tracks_spider -a start_url={band_home_page} -a band_name={band_name}'
command_2 = f'scrapy crawl lyrics_spider -a band_name={band_name} -o data/{band_name}_lyrics.json -t json'

os.system(command_1)
os.system(command_2)