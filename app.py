# website navigation imports
from flask import Flask, render_template, request, flash, Markup # webpage interaction
from bs4 import BeautifulSoup # website text fetcher
import requests # website fetcher
import html.parser
from unidecode import unidecode
# keywords per attribute
base = 'https://www.atlasobscura.com/things-to-do/'
sKey = ['medic', 'scien', 'museum', 'onomer', 'olog', 'atom', 'mutant', 'body']
hKey = ['cemetery', 'remains', 'abandon', 'museum', 'hist', 'old', 'war', 'past', 'first','restored', 'world', 'church']
aKey = ['art', 'beautiful', 'poe', 'mosaic', 'mural', 'paint', 'iconic', 'glass', 'music']
nKey = ['water', 'natur', 'garden', 'cave', 'forest', 'cave', 'rock', 'park', 'wood', 'mt', 'world', 'caverns', 'tree']
eKey = ['!', 'fiction', 'fame', 'entert', 'enjoy', 'amuse', 'park', 'museum']

# website base requirements
app = Flask(__name__)
app.secret_key='squid'

# instruction page
@app.route("/")
def index():
    flash('Please enter the location you would like to search.')
    flash('The question marks provide guidance if necessary.')
    return render_template("index.html")

# search page
@app.route("/search", methods=["POST", "GET"]) # getting info from html, posting info to site
def search():
    try:
        # fetch user input
        location = request.form['location'].lower()
        attributes = []
        try:
            attributes.append(request.form['scienceR'])
        except:
            attributes.append('no')
        try:
            attributes.append(request.form['historyR'])
        except:
            attributes.append('no')
        try:
            attributes.append(request.form['artR'])
        except:
            attributes.append('no')
        try:
            attributes.append(request.form['natureR'])
        except:
            attributes.append('no')
        try:
            attributes.append(request.form['entertainmentR'])
        except:
            attributes.append('no')
        page = site(location)
        # checks for 404 error
        if page != BeautifulSoup(requests.get('https://www.atlasobscura.com/404').text, 'html.parser').get_text() and location.find('-') == -1:
            isolate(page, location)
            display = classify(attributes)
            filter(display)
        else:
            flash('PAGE NOT FOUND. Please check your spelling and format, then try again.')
    except:
        flash('CONNECTION FAILED. Your signal is too weak to support the program.')
        flash('Please acquire a stronger connection and try again.')
    return render_template("index.html")
    
def site(location):
    # format text into url
    return BeautifulSoup(requests.get(base+location.replace(", ", "-")+'/places').text, 'html.parser').get_text()
    
def isolate(page, location):
    # isolate attraction information
    start = page.find('Recently Added')
    end = page.find('Are we missing something unusual')
    if end == -1:
        end = page.find('\n1\n')
        if end == -1:
            end = page.find('Get Our Email Newsletter')   
    info = page[start+15:end]
    # format attraction information into uniform pattern
    info = info.replace('\n\n', '')
    info = info.lower()+'\n'
    if location.find(', ') != -1:
        info = info.replace(location, location+'\n')
    else:
        info = info.replace(', '+location, ', '+location+'\n')
        info = info.replace('.\n'+location, '.\n'+location+'\n')
    count = 1
    global attractions
    global descriptions
    attractions = []
    descriptions = []
    attraction = ''
    description = ''
    # sort info into location, attraction, and description categories
    for x in info:
        if x != '\n':
            if count == 2:
                attraction += x
            else:
                description += x
        else:
            if count == 1:
                count += 1
            elif count == 2:
                attractions.append(attraction)
                attraction = ''
                count += 1
            else:
                descriptions.append(description)
                description = ''
                count = 1

def classify(attributes):
    sCount = 0
    hCount = 0
    aCount = 0
    nCount = 0
    eCount = 0
    display = {}
    # search attraction name and description for given attribute keywords
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
        total = sCount + hCount + aCount + nCount + eCount
        results = []
        # generates dictionary of attraction : percent match
        for y in range(len(attributes)):
            if attributes[y] == 'on' and y == 0:
                try:
                    results.append(sCount/total)
                except:
                    results.append(0.0)
            if attributes[y] == 'on' and y == 1:
                try:
                    results.append(hCount/total)
                except:
                    results.append(0.0)
            if attributes[y] == 'on' and y == 2:
                try:
                    results.append(aCount/total)
                except:
                    results.append(0.0)
            if attributes[y] == 'on' and y == 3:
                try:
                    results.append(nCount/total)
                except:
                    results.append(0.0)
            if attributes[y] == 'on' and y == 4:
                try:
                    results.append(eCount/total)
                except:
                    results.append(0.0)
        sCount = 0
        hCount = 0
        aCount = 0
        nCount = 0
        eCount = 0
        display[attractions[x].upper()] = results
        results = []
    return display

def filter(display):
    # display to website
    percents = list(display.values())
    attractions = list(display.keys())
    check = False
    # checks for attribute request
    if [] not in percents:
        for x in range(len(percents)):
            # display nonzero percent matches
            if 0.0 not in percents[x]:
                val = attractions[x] + ': '+ str(format(sum(percents[x])/len(percents[x])*100, '.2f')) + '% MATCH'
                flash(Markup('<a href="https://www.atlasobscura.com/places/')+unidecode(attractions[x].replace(' ', '-').lower().replace('\'', '')+Markup('"class="alert-link">')+val+Markup('</a>')))
                check = True
        # check for matches
        if check == False:
            flash('NO MATCHES. Try selecting less attributes.')
    else:
        for x in range(len(attractions)):
            flash(Markup('<a href="https://www.atlasobscura.com/places/')+unidecode(attractions[x].replace(' ', '-').lower().replace('\'', '')+Markup('"class="alert-link">')+attractions[x]+Markup('</a>')))# display