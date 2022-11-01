import requests
from bs4 import BeautifulSoup

root = "https://www.mtggoldfish.com"
player = input("Enter MTGO name: ")
firstPage = requests.get(root + "/player/" + player)
firstSoup = BeautifulSoup(firstPage.text, 'html.parser')
pages = []

for link in firstSoup.find_all('a'):
    if player in link.get("href"):
        pages.append(link.get("href"))
pages.pop()

def getDecksOffPage(url):
    r = requests.get(url)
    links = []
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        if "/deck/" in link.get("href"):
            if "Submitted" not in link.text:
                links.append(link.text)
    return links


def printBreakdown(deckLists):
    deckOccurences = {}
    for deck in deckLists:
        if deck in deckOccurences:
            deckOccurences[deck] = deckOccurences[deck] + 1
        else:
            deckOccurences[deck] = 1
    print(dict(sorted(deckOccurences.items(), key=lambda item: item[1])))

decklists = []
for page in pages:
   decklists += getDecksOffPage(root + page)

printBreakdown(decklists)