# program should allow user to search for attractions in an area
import tkinter

class selection:
  def __init__(self):
    # creates and organizes main window
    self.mainWindow = tkinter.Tk()

    self.initalFrame = tkinter.Frame(self.mainWindow)
    self.scopeFrame = tkinter.Frame (self.mainWindow)
    self.firstFrame = tkinter.Frame(self.mainWindow)
    self.secondFrame = tkinter.Frame(self.mainWindow)
    self.thirdFrame = tkinter.Frame(self.mainWindow)
    self.initalFrame.pack()
    self.scopeFrame.pack()
    self.firstFrame.pack()
    self.secondFrame.pack()
    self.thirdFrame.pack()

    # describes purpose and use of program
    self.introduction = tkinter.Label(self.initalFrame, text='This program allows you to search for attractions in an area based\n on the kind of attraction you would like to see! First, select a scope: \n(as the scope increases, less popular attractions will be cut to fit the new scope).')
    self.introduction.pack()

    # allows user to select search scope
    self.radio = tkinter.IntVar()
    self.radio.set(1)

    self.state = tkinter.Radiobutton(self.scopeFrame, text='Pennsylvania', variable=self.radio, value=1)
    self.region = tkinter.Radiobutton(self.scopeFrame, text='Central/Southern Counties', variable=self.radio, value=2)
    self.state.pack(side='left')
    self.region.pack(side='left')

    # instruction of use continues
    self.instructions = tkinter.Label(self.firstFrame, text='Next, please select all desired attributes for the search! \nThese affect what kind of attractions you will see.')
    self.instructions.pack()

    # allows user to select search attributes
    self.sci = tkinter.IntVar()
    self.art = tkinter.IntVar()
    self.nat = tkinter.IntVar()
    self.ent = tkinter.IntVar()
    self.his = tkinter.IntVar()

    self.sci.set(0)
    self.art.set(0)
    self.nat.set(0)
    self.ent.set(0)
    self.his.set(0)

    self.science = tkinter.Checkbutton(self.secondFrame, text='Science', variable=self.sci)
    self.artistic = tkinter.Checkbutton(self.secondFrame, text='Art', variable=self.art)
    self.nature = tkinter.Checkbutton(self.secondFrame, text='Nature', variable=self.nat)
    self.entertainment = tkinter.Checkbutton(self.secondFrame, text='Entertainment', variable=self.ent)
    self.history = tkinter.Checkbutton(self.secondFrame, text='History', variable=self.his)

    self.science.pack(side='left')
    self.artistic.pack(side='left')
    self.nature.pack(side='left')
    self.entertainment.pack(side='left')
    self.history.pack(side='left')

    # creates buttons to initate and quit program
    self.search = tkinter.Button(self.thirdFrame, text='Search!', command=self.find)
    self.quit = tkinter.Button(self.thirdFrame, text='Quit', command=self.mainWindow.destroy)

    self.search.pack(side='left')
    self.quit.pack(side='left')

    global choices
    choices = 0

    # displays main window
    tkinter.mainloop()
  def find(self):
    # distributes choices to program and allows main to continue
    global choices
    choices = [self.sci.get(), self.art.get(), self.nat.get(), self.ent.get(), self.his.get(), self.radio.get()]
    self.mainWindow.destroy()

# master function
def main():
  selection()
  # checks if no attributes were selected to begin search
  if choices:
    assignment(choices)
    attribute = call(choices)
    codification = codify(attribute)
    if len(attribute) > 1:
      valid = filter(codification, attribute)
    else:
      valid = codification
    display(valid)

# diplay results of the program
def display(valid):
  # list attractions that fit given attributes, if any
  if valid != []:
    mainWindow = tkinter.Tk()
    firstFrame = tkinter.Frame(mainWindow)
    secondFrame = tkinter.Frame(mainWindow)
    thirdFrame = tkinter.Frame(mainWindow)

    preface = tkinter.Label(firstFrame, text='Here are the attractions that fit the given attributes:')
    preface.pack()

    box = tkinter.Listbox(secondFrame)
    count = 0
    for x in valid:
      box.insert(count, x)
      count += 1
    box.pack(side='right')
    box.config(width=50)

    # the home button breaks the mainloop and recalls the main function
    home = tkinter.Button(thirdFrame, text='Home', command=mainWindow.destroy)

    home.pack()

    firstFrame.pack()
    secondFrame.pack()
    thirdFrame.pack()

    tkinter.mainloop()
    main()
  else:
    # if there are no valid attributes, open this error window
    mainWindow = tkinter.Tk()
    topFrame = tkinter.Frame(mainWindow)
    bottomFrame = tkinter.Frame(mainWindow)
    topFrame.pack()
    bottomFrame.pack()

    error = tkinter.Label(topFrame, text='Sorry, no attractions fit the specified attributes.')
    error.pack()

    # back button also breaks the mainloop and recalls the main function
    back = tkinter.Button(bottomFrame, text='Home', command=mainWindow.destroy)
    back.pack()

    tkinter.mainloop()
    main()

# find attractions shared between attributes
def filter(codification, attribute):
  valid = []
  # sorting algorithm
  # Iterates over two positions of the list and compares to see if they're the same
  for x in range(len(codification)):
    count = 1
    for y in range(len(codification)):
      if codification[x] == codification[y] and x != y:
        count += 1
        if count == len(attribute):
          valid.append(codification[x])
  valid = list(set(valid))
  return valid

# find relevant attractions with the given attribute
def codify(attribute):
  # appends the information from a file to a list
  codification = []
  for x in attribute:
    infile = open(x, 'r')
    file = infile.read()
    infile.close()
    attraction = ''
    for x in file:
      if x != '-':
        attraction += x
      else:
        codification.append(attraction)
        attraction = ''
  return codification 

# define attributes
def call(choices):
  # mechanism to determine which attributes were requested
  attribute = []
  if choices[4] == 1:
    attribute.append('historic.txt')
  if choices[2] == 1:
    attribute.append('nature.txt')
  if choices[3] == 1:
    attribute.append('entertainment.txt')
  if choices[0] == 1:
    attribute.append('science.txt')
  if choices[1] == 1:
    attribute.append('art.txt')
  return attribute

# define attractions
def assignment(choices):
  # determines the scope of the search and assigns available attractions accordingly
  if choices[5] == 1:
    infile = open('historic.txt', 'w')
    infile.write('Eastern State Penitentiary-Pennsylvania State Capitol Complex-Gettysburg National Military Park-Valley Forge National Historic Park-Mount Moriah Cemetery-Independence National Historic Park / Liberty Bell-Mercer Museum-Fonthill Castle-State Museum of Pennsylvania-Rivers of Steel National Heritage Area-Lackawanna Coal Mine-National Civil War Museum-Flight 93 Memorial-Eisenhower National Historic Site-Steamtown National Historic Site-Horseshoe Curve-')
    infile.close()
    infile = open('nature.txt', 'w')
    infile.write('Fallingwater-Phipps Conservatory-Philadelphia’s Magic Gardens-Cave of Kelpius-Carnegie Museum of Natural History-Shofuso Japanese House and Garden-Ringing Rocks Park-Penn’s Cave-Longwood Gardens-Indian Echo Caverns-Brandywine Conservancy-Lake Tobias Wildlife Park-Chanticleer-Presque Isle State Park-Horseshoe Curve-Philadelphia Zoo-')
    infile.close()
    infile = open('entertainment.txt', 'w')
    infile.write('Hersheypark-Dutch Wonderland-Philadelphia Zoo-Sight and Sound Theatres-The Hershey Story-King of Prussia Mall-The Weeping Glass-')
    infile.close()
    infile = open('science.txt', 'w')
    infile.write('Mutter Museum-Phipps Conservatory-Carnegie Museum of Natural History-Trundle Manor: House of Oddities-Franklin Institute-Longwood Gardens-State Museum of Pennsylvania-Railroad Museum of Pennsylvania-Wagner Free Institute of Science-Steamtown National Historic Site-')
    infile.close()
    infile = open('art.txt', 'w')
    infile.write('Andy Warhol Museum-Fallingwater-Philadelphia Museum of Art-Rodin Museum-Trundle Manor: House of Oddities-Wharton Esherick Museum-Barnes Foundation-State Museum of Pennsylvania-Susquehanna Art Museum-Brandywine River Museum of Art-Edgar Allen Poe National Historic Site-Randyland-')
    infile.close()
  else:
    infile = open('historic.txt', 'w')
    infile.write('Gallitzin Tunnels Park and Museum-Horseshoe Curve-Old Bedford Village Shoppes-Koontz Coffee Pot-Coral Caverns-Paw Paw Tunnel-The National Museum of the American Coverlet-East Broad Top Railroad-Ironstone Ranch-Heritage Discovery Center-Talleyrand Park-')
    infile.close()
    infile = open('nature.txt', 'w')
    infile.write('Buttermilk Falls Natural Area-Hawn’s Overlook-Mount Assisi Gardens-Penn’s Cave & Wildlife Park-Horseshoe Curve-Coral Caverns-Paw Paw Tunnel-Living Waters Camp-Cowans Gap State Park-Lincoln Caverns-Thousand Steps-Black Moshannon State Park-Shaver’s Creek Environmental Center-Raystown Lake-Living Treasures Animal Park-Bilgers Rocks-Woodward Cave-Bald Eagle State Park-Arboretum at Penn State-T&D’s Cat’s of the World-Kish Park-Lake Tobias State Park-Poe Valley State Park-Juniata River Adventures-Little Buffalo State Park-Echo Dell Indian Echo Caverns-Ironstone Ranch-Talleyrand Park-Reed’s Gap State Park-')
    infile.close()
    infile = open('entertainment.txt', 'w')
    infile.write('Slinky Action Zone-DelGrosso’s Park and Laguana Splash-Escape Rooms Altoona-Urban Air Adventure Park-Living Waters Camp-Heavy Metal Playground-Mister Ed’s Elephant Musuem and Candy Emporium-Shaver’s Creek Environmental Center-Living Treasures Animal Park-Happy Valley Minigolf-Central Pennsylvania Festival of the Arts-T&D’s Cat’s of the World-Hoopla’s Xtreme-Kish Park-Juniata River Adventures-Midway Theater Drive In-Bounce Away Funplex and Mini golf-Dream Castle Entertainment-')
    infile.close()
    infile = open('science.txt', 'w')
    infile.write('Lincoln Caverns-Woodward Cave-Central Pennsylvania Festival of the Arts-Discovery Space of Central PA-')
    infile.close()
    infile = open('art.txt', 'w')
    infile.write('Central Pennsylvania Festival of the Arts-Heart of Steel Designs-Echo Dell Indian Echo Caverns-Tiny World-')
    infile.close()
main()
