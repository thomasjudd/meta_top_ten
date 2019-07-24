#!/usr/bin/python
from lxml import html
import requests
import json
import time
import re

games_base_url = "http://www.dicetower.com"

collection_base_url = 'http://www.dicetower.com/video-category/top-10'

#sufficiently large number for testing purposes
game_pages = []


def get_game_link_on_page(page):
    tree = html.fromstring(page.content)
    page = tree.xpath('//h2/a/@href')
    return page

# crappy initialization so they are different
prev_game_page = -1
curr_game_page = -2

count = 1

while prev_game_page != curr_game_page:
  page = requests.get(collection_base_url + '?page='+ str(count))
  time.sleep(5)
  print(collection_base_url + '?page='+ str(count))
  game_page = get_game_link_on_page(page)
  prev_game_page = curr_game_page
  curr_game_page = game_page
  game_pages.extend(game_page)
  count += 1

games = {}

for game_page in game_pages:
  page = requests.get(games_base_url+game_page)
  time.sleep(5)
  print(games_base_url+game_page)

  tree = html.fromstring(page.content)
  game_titles = tree.xpath('//div[@class="gt_title"]/a/text()')

  print(game_titles)
  if len(game_titles) > 1:
    for title in game_titles:
      if not title in games.keys():
        games[title] = 1
      else:
        games[title] += 1 

json.dump(games, open("games.json", "w"))
