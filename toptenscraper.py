#!/usr/bin/python
from lxml import html
import requests
import json
import time
import re

games_base_url = "http://www.dicetower.com"

collection_base_url = 'http://www.dicetower.com/video-category/top-10'

numpages = 15
game_pages = []
for i in range(1, numpages):
  page = requests.get(collection_base_url + '?page='+ str(i))
  time.sleep(2)
  print collection_base_url + '?page='+ str(i)
  tree = html.fromstring(page.content)
  game_page = tree.xpath('//h2/a/@href')
  game_pages.extend(game_page)

games = {}

for game_page in game_pages:
  page = requests.get(games_base_url+game_page)
  time.sleep(2)
  print games_base_url+game_page

  tree = html.fromstring(page.content)
  game_titles = tree.xpath('//div[@class="gt_title"]/a/text()')

  print game_titles
  if len(game_titles) > 1:
    for title in game_titles:
      if not title in games.keys():
        games[title] = 1
      else:
        games[title] += 1 

json.dump(games, open("games.json", "w"))
