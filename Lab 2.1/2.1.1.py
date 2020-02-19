import json
import pprint
import requests
import time
import os
import sys

card_bank = []
for card_no in sys.argv[1:]:
    r = requests.get('https://lookup.binlist.net/'+card_no, headers={'Accept-Version': "3"})
    if 200 <= r.status_code <= 299:
        card_info = r.json()
        card_bank.append(card_info['bank']['name'])
print (card_bank)