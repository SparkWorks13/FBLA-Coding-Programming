#here we go again
# Create 5 files, each corresponding to an attribute, and containing the relevant attractions.
# Request input from the user, which asks for 1 or more attributes
# Open relevant files
# Check for repeats, remove as needed
# Display results
# prepare GUI
import tkinter

class selection:
  def __init__(self):
    #main window
    self.mainWindow = tkinter.Tk()

    self.firstFrame = tkinter.Frame(self.mainWindow)
    self.secondFrame = tkinter.Frame(self.mainWindow)
    self.thirdFrame = tkinter.Frame(self.mainWindow)
    self.firstFrame.pack()
    self.secondFrame.pack()
    self.thirdFrame.pack()

    self.instructions = tkinter.Label(self.firstFrame, text='Please select all desired attributes for the search!')
    self.instructions.pack()

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

    self.search = tkinter.Button(self.thirdFrame, text='Search!', command=self.find)
    self.quit = tkinter.Button(self.thirdFrame, text='Quit', command=self.mainWindow.destroy)

    self.search.pack(side='left')
    self.quit.pack(side='left')

    global choices
    choices = 0

    #open
    tkinter.mainloop()
  def find(self):
    global choices
    choices = [self.sci.get(), self.art.get(), self.nat.get(), self.ent.get(), self.his.get()]
    self.mainWindow.destroy()


# call the functions
def main():
  selection()
  if choices:
    assignment()
    attribute = call(choices)
    codification = codify(attribute)
    if len(attribute) > 1:
      valid = filter(codification, attribute)
    else:
      valid = codification
    display(valid)

# diplay attractions
def display(valid):
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

    home = tkinter.Button(thirdFrame, text='Home', command=mainWindow.destroy)

    home.pack()

    firstFrame.pack()
    secondFrame.pack()
    thirdFrame.pack()

    tkinter.mainloop()
    main()
  else:
    mainWindow = tkinter.Tk()
    topFrame = tkinter.Frame(mainWindow)
    bottomFrame = tkinter.Frame(mainWindow)
    topFrame.pack()
    bottomFrame.pack()

    error = tkinter.Label(topFrame, text='Sorry, no attractions fit the specified attributes.')
    error.pack()

    back = tkinter.Button(bottomFrame, text='Home', command=mainWindow.destroy)
    back.pack()

    tkinter.mainloop()
    main()

# find common attractions
def filter(codification, attribute):
  valid = []
  for x in range(len(codification)):
    count = 1
    for y in range(len(codification)):
      if codification[x] == codification[y] and x != y:
        count += 1
        if count == len(attribute):
          valid.append(codification[x])
  valid = list(set(valid))
  return valid

# find relevant attractions
def codify(attribute):
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
def assignment():
  infile = open('historic.txt', 'w')
  infile.write('Eastern State Penitentiary-Pennsylvania State Capitol Complex-Gettysburg National Military Park-Valley Forge National Historic Park-Mount Moriah Cemetery-Independence National Historic Park / Liberty Bell-Mercer Museum-Fonthill Castle-State Museum of Pennsylvania-Rivers of Steel National Heritage Area-Lackawanna Coal Mine-National Civil War Museum-Flight 93 Memorial-Eisenhower National Historic Site-Steamtown National Historic Site-')
  infile.close()
  infile = open('nature.txt', 'w')
  infile.write('Fallingwater-Phipps Conservatory-Philadelphia’s Magic Gardens-Cave of Kelpius-Carnegie Museum of Natural History-Shofuso Japanese House and Garden-Ringing Rocks Park-Penn’s Cave-Longwood Gardens-Indian Echo Caverns-Brandywine Conservancy-Lake Tobias Wildlife Park-Chanticleer-Presque Isle State Park-')
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

main()
