import json
import pprint
import requests
import time
import os

#card_no = "47148700"
card_list = set()


dirs = os.listdir()
print (dirs)

cards_no = []
#if ".json" in dirs:

with open("card1.json") as f:
    cards = json.load(f)
    for card in cards:
        cards_no.append(str(card['CreditCard']['CardNumber'])[:8])

print (cards_no)

for card_no in cards_no:
    r = requests.get('https://lookup.binlist.net/'+card_no, headers={'Accept-Version': "3"})
#pprint.pprint(r.json())
    if 200 <= r.status_code <= 299:
        card_info = r.json()
        card_list.add(card_info['bank']['name'])
    time.sleep (3)
print (sorted(card_list))