from googlesearch import search
from bs4 import BeautifulSoup
import requests
import html.parser

base = 'https://www.atlasobscura.com/things-to-do/'
sKey = ['medic', 'scien', 'museum', 'onomer', 'olog', 'atom', 'mutant', 'body']
hKey = ['cemetery', 'remains', 'abandon', 'museum', 'hist', 'old', 'war', 'past', 'first','restored', 'world', 'church']
aKey = ['art', 'beautiful', 'poe', 'mosaic', 'mural', 'paint', 'iconic', 'glass', 'music']
nKey = ['water', 'natur', 'garden', 'cave', 'forest', 'cave', 'rock', 'park', 'wood', 'mt', 'world', 'caverns', 'tree']
eKey = ['!', 'fiction', 'fame', 'entert', 'enjoy', 'amuse', 'park', 'musuem']
def main():
    location = 'pittsburgh-pennsylvania'
    page = site(location)
    isolate(page)
    classify()
    
def site(location):
    return BeautifulSoup(requests.get(base+location+'/places').text, 'html.parser').get_text()
    
def isolate(page):
    start = page.find('Recently Added')
    end = page.find('Are we missing something unusual')
    if end == -1:
        end = page.find('\n1\n')
    info = page[start+15:end]
    info = info.replace('\n\n', '')
    info = info.replace(', Pennsylvania', ', Pennsylvania\n')
    info = info.lower()+'\n'
    count = 1
    global locations
    global attractions
    global descriptions
    locations = []
    attractions = []
    descriptions = []
    location = ''
    attraction = ''
    description = ''
    for x in info:
        if x != '\n':
            if count == 1:
                location += x
            elif count == 2:
                attraction += x
            else:
                description += x
        else:
            if count == 1:
                locations.append(location)
                location = ''
                count += 1
            elif count == 2:
                attractions.append(attraction)
                attraction = ''
                count += 1
            else:
                descriptions.append(description)
                description = ''
                count = 1

def classify():
    sCount = 0
    hCount = 0
    aCount = 0
    nCount = 0
    eCount = 0
    for x in range(len(attractions)):
        for y in range(len(sKey)):
            if sKey[y] in attractions[x]:
                sCount += 1
            if sKey[y] in descriptions[x]:
                sCount += 1
        for y in range(len(hKey)):
            if hKey[y] in attractions[x]:
                hCount += 1
            if hKey[y] in descriptions[x]:
                hCount += 1
        for y in range(len(aKey)):
            if aKey[y] in attractions[x]:
                aCount += 1
            if aKey[y] in descriptions[x]:
                aCount += 1
        for y in range(len(nKey)):
            if nKey[y] in attractions[x]:
                nCount += 1
            if nKey[y] in descriptions[x]:
                nCount += 1
        for y in range(len(eKey)):
            if eKey[y] in attractions[x]:
                eCount += 1
            if eKey[y] in descriptions[x]:
                eCount += 1
        print(attractions[x].upper()+ ': '+ str(sCount)+ str(hCount)+ str(aCount)+ str(nCount)+ str(eCount))
        sCount = 0
        hCount = 0
        aCount = 0
        nCount = 0
        eCount = 0
main()
