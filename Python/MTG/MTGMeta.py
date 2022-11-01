from re import L
import requests
from bs4 import BeautifulSoup

root = "https://www.mtggoldfish.com"
format = (input("What format do you want to know the meta for? ")).lower()
r = requests.get(root + "/metagame/" + format)
soup = BeautifulSoup(r.text, 'html.parser')
deckLists = []

links = soup.find_all('a')
tlinks = []
for link in links:
    string_link = str(link)
    if "tournament" in string_link:
        tlinks.append(link.get('href'))
tlinks = tlinks[3:-1]

for link in tlinks:
    r = requests.get(root + link)
    soup = BeautifulSoup(r.text, "html.parser")
    for list in soup.find_all('a'):
        if "archetype" in str(list):
            deckLists.append(list.text)

deckOccurences = {}

for deck in deckLists:
    if deck in deckOccurences:
        deckOccurences[deck] = deckOccurences[deck] + 1
    else:
        deckOccurences[deck] = 1

print(dict(sorted(deckOccurences.items(), key=lambda item: item[1])))