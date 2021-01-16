import time, random, os, sys

white = "\033[0;37m"
yellow = "\033[0;93m"
red = "\033[1;31m"
green = "\033[0;32m"
blue = "\033[0;94m"
italicgreen = "\033[3;32m"
sp = 0.03

adan = []
an = ["lion cub","baby orangutan","seal pup"]
nav = ["Adoption Centre","Home"]
everything = ["Home","Adoption Centre","lion cub","baby orangutan","seal pup'"]

def clear():
  os.system('clear') 

def enter():
  input(white+'\nPress '+green+'ENTER '+white+'to continue.')

def scroll(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(sp)
  print()

def home():
  if (len(adan) == 0):
    scroll(white+"Oh No! It looks like you havn't got any adopted animals,\nwhy not go to the adoption centre to adopt some?")
    enter()

  else:
    print("You have " + str(len(adan)) + " adopted animals")
    enter()

  nav.remove("Home")
  nava = input("\nWhere would you like to go?\n" + str(nav) + "\n--> "+yellow)
  nav.append("Home")
  index = everything.index(nava)
  if (index == 0):
    clear()
    home()
  if (index == 1):
    clear()
    adoptioncentre()
  if (index == 2):
    clear()
    lioncub()
  if (index == 3):
    clear()
    babyorangutan()
  if (index == 4):
    clear()
    sealpup()

def adoptioncentre():
  scroll(white+"Hi! Welcome to the adoption centre!")
  enter()
  nava = input("\nHow can I help you?\n1. Adopt my first animal\n--> "+yellow)
  if (nava == "1"):
    scroll(white+"\nHere is your free gift!")
    scroll("\n...I can't wait...")
    scroll("\n...I wonder what it will be...")
    scroll("\n...Here it is...")
    enter()
    clear()
    newadan = an[random.randint(0,2)]
    scroll("You adopted a " + newadan + "!")
    adan.append(newadan)
    nav.append(newadan)
    nav.remove("Adoption Centre")
    nava = input("\nWhere would you like to go?\n" + str  (nav) + "\n-->"+yellow)
    nav.append("Adoption Centre")
    index = everything.index(nava)
    if (index == 0):
      clear()
      home()
    if (index == 1):
      clear
      adoptioncentre()
    if (index == 2):
      clear()
      lioncub()
    if (index == 3):
      clear()
      babyorangutan()
    if (index == 4):
      clear()
      sealpup()

def lioncub():
  print("lion cub")

def babyorangutan():
  print(babyorangutan)

def sealpup():
  print("seal pup")

scroll(white+"Hi! I'm Zazee, welcome to the zoo!\n")
home()