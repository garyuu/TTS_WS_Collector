"""
============================================================
@ Main
============================================================
Date: 2016/11/30
Author: Garyuu
Usage: Auto grap a series of WS cards' content and graphics.
============================================================
"""

import urllib.request
import library.card
import os

text_source = "http://ws-tcg.com/cardlist/"
graphic_source = "http://www.cardbox.sc/img/card/wsz/"

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

os.mkdir(series_head)
text_page = "{}?cardno={}-{:03}".format(text_source, series_head, series_start)
print(text_page)
#resp = urllib.request.urlopen(text_page)
#content = resp.read()
