# FBLA-Coding-Programming
Catalog of various iterations of the code I wrote for the 2021-2022 FBLA Coding and Programming Competition.

The prompt for this year was to develop an application which would allow user to search for and filter attractions in a given area.

**Regionals + States**

*fbla.py* script was my first attempt, submitted for the regional competition. It uses Python's Tkinter module to create a graphical interface, through which the user can select their desired attributes and search for attractions from a predetermined list. 

Before the state competition, I cleaned it up, producing *attractionSearch.py*, which is logically identical, but properly documented.

**Nationals**

For the national competition, I wanted to interface the program to a website, instead of using Tkinter as a frontend. For this, I set up a virtual environment in Python and used the Flask module to develop the website.

It should be noted that the files listed here do not comprise the virtual environment, only the python backend and html+css frontend.
The idea was to create a webscraper which would pull data off a given site and filter it by keywords, which would categorize the attractions based on how the user selected their filters.

It should also be noted that I don't think this code works anymore, due to the source website having changed their policies; but the idea is there.

My first attempt took the form of *finale.py*, which was not, in fact, the finale. This used the import Beautiful Soup to scrape the website and printed data to the user; I was still getting my bearings, and struggling to get flask working.

*app.py* is the final website backend. *index.html* and *main.css* comprise the frontend.

Don't use Flask. Just learn JavaScript.
