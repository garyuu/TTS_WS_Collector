"""
============================================================
@ Main
============================================================
Date: 2016/11/30
Author: Garyuu
Usage: Auto grap a series of WS cards' content and graphics.
============================================================
"""

import os
import urllib.request
from bs4 import BeautifulSoup
# Custumized modules
from library.card import Card

text_source = "http://ws-tcg.com/cardlist/"
graphic_source = "http://www.cardbox.sc/img/card/wsz/"

def parse_card_info(html):
    result = Card()
    soup = BeautifulSoup(html, "html.parser")
    info_data = soup.find('table', class_="status").find_all('tr')
    result.official_image = "http://ws-tcp.com" + info_data[0].find('td', class_="graphic").img['src']
    result.name = info_data[0].find('td', colspan="3").contents[0]
    result.id = info_data[1].find('td', class_='cell_2').contents[0]
    result.rarity = info_data[1].find('td', class_='cell_4').contents[0]
    result.expansion = info_data[2].find('td').contents[0]
    result.side = info_data[2].find('img')['src'][-5]
    result.type = info_data[3].find('td').contents[0]
    result.color = info_data[3].find('img')['src'].split('/')[-1][:-4]
    result.level = info_data[4].find('td').contents[0]
    result.cost = info_data[4].find_all('td')[1].contents[0]
    result.power = info_data[5].find('td').contents[0]
    result.soul = len(info_data[5].find_all('td')[1].find_all('img'))
    result.trigger = len(info_data[6].find('td').find_all('img'))
    result.attribute = info_data[6].find_all('td')[1].contents[0].split()
    result.attribute.remove(result.attribute[1])
    result.text = info_data[7].find('td').contents
    for t in result.text:
        if not isinstance(t, str):
            result.text.remove(t)
    return result

def direction_assign(name):
    os.mkdir(series_head)

def downloader(head, start, finish):
    save_dir = direction_assign(head)
    urllib.request.urlopen(text_source)
    for i in range(start, finish+1):
        # Try to download the card info, if Html error then break.
        # If no such card ID, find next.
        text_url = "{}?cardno={}-{:03}".format(text_source, head, i)
        try:
            resp = urllib.request.urlopen(text_url)
        except:
            print("Error: Can't find series {}.".format(head))
            break
        text_page = resp.read()
        if text_page.find("expansionAnchor") == -1:
            print("Error: Can't find card {}-{:03}.".format(head, i))
            continue
        # Now text_page is a page with card info
        card = parse_card_info(text_page)
        # Find card image from cardbox. if there's no result, 
        

def main():
    print("\nWelcome to WS card grabber!")
    print("It's a simple tool without error detection.")
    print("Will crash if you enter something with incorrect format.")
    print("\n--")

    print("\nPlease enter a series ID head.")
    print("For example, if a card in a series with ID = KC/S25-001,")
    print("you should enter KC/S25.")
    series_head = input(">>> Series: ")

    print("\nPlease enter the range of card ID.")
    print("For example, Kancolle series has ID from KC/S25-001 to KC/S25-164")
    print("you should enter 1 first then 164.")
    series_start = int(input(">>> From: "))
    series_finish = int(input(">>> To: "))
    downloader(series_head, series_start, series_finish)

"""
url = "http://ws-tcg.com/cardlist/?cardno=KC/S25-004"
resp = urllib.request.urlopen(url)
html = resp.read()
card = parse_card_info(html)
print(card.id)
print(card.name)
print(card.rarity)
print(card.side)
print(card.expansion)
print(card.type)
print(card.color)
print(card.level)
print(card.cost)
print(card.power)
print(card.soul)
print(card.trigger)
print(card.attribute)
print(card.text)
print(card.official_image)
"""
"""
soup = BeautifulSoup(html, 'html.parser')
lines = soup.find('table', class_="status").find_all('tr')
name = lines[0].find_all('td')[1]
print(name.contents[0])
"""
