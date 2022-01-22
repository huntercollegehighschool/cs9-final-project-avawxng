"""
Name(s): Ava Wong
Name of Project: "Regrets: The End of the World"
"""
import os
import time

def start(): 
  print("You wake up. Eyes blinking open, you register your bedroom— closed curtains, desk, and everything. It's still dark outside.")
  time.sleep(3)
  print("\nGroggily, you look to the side. You look at the calendar. There is one thing going on today. In bold, black letters, you spy the text: The End of the World")
  time.sleep(3.5)
  print("\nYou make your way out of bed, changing into your day clothes.")
  time.sleep(2)
  decision1 = input("\nPress B to make breakfast, C to call someone, and L to leave your house: ")
  
  while decision1 != "B" and decision1 != "C" and decision1 != "L":
    print("Not a valid answer.")
    decision1 = input("\nPress B to make breakfast, C to call a friend, and L to leave your house: ")
  if decision1 == "B": 
    choicebreakfast()
  elif decision1 == "C": 
    choice2callsomeone()
  elif decision1 == "L":
    choice2leavehouse()

#Option 1: the 'ordinary' options
def choicebreakfast():
  os.system('clear')
  print("There's really nothing major going on today. So, you decide to make breakfast first. After all, it's the best way to start the day.")
  time.sleep(3)
  print("\nYou make yourself a cup of coffee, then grab two eggs from your fridge. You grab a pot, add water, and begin to boil your eggs.")
  time.sleep(3)
  decisionbreakfast = input("\nYou distantly register your phone buzzing, but your eggs are almost done. Press C to check your phone, and W to wait for your eggs: ")
  
  while decisionbreakfast != "C" and decisionbreakfast != "W":
    print("Not a valid answer.")
    decisionbreakfast = input("\nPress C to check your phone, and W to wait for your eggs: ")
  if decisionbreakfast == "C":
    choicecheck()
  elif decisionbreakfast == "W": 
    choicewaitingforegg()

def choicecheck():
  os.system('clear')
  print("Curious, you check your phone. When you open it, you see notifcations from every major new source, calls, messages, emails— what's going on??")
  time.sleep(3)
  decisioncheck = input("\nYou have to do something! Press L to leave your house or C to call someone: ")

  while decisioncheck != "L" and decisioncheck != "C": 
    print("Not a valid answer.")
    decisioncheck = input("\nPress L to leave your house or C to call someone: ")
  if decisioncheck == "L": 
    choice2leavehouse()
  elif decisioncheck == "C":
    choice2callsomeone()

def choicewaitingforegg():
  os.system('clear')
  print("You don't want to ruin your soft boiled eggs! Ignoring the phone call, you wait until your eggs are done.")
  time.sleep(2.5)
  print("\nThen, once finished, you sit down at your table, eggs in front of you, coffee in hand.")
  time.sleep(2)
  decisionwait = input("\nYou want to do something as you eat. Press R to read a book and T to turn on the TV: ")

  while decisionwait != "R" and decisionwait != "T":
    print("Not a valid answer.")
    decisionwait = input("\nPress R to read a book or T to turn on TV: ")
  if decisionwait == "R": 
    choicebook()
  elif decisionwait == "T":
    choiceturnontv()

def choicebook():
  os.system('clear')
  print("\nYou decide to read a book as you eat your perfectly soft boiled egg. You open it to your last page, and get lost in the words for a couple hours.")
  time.sleep(3)
  print("\nYou finish your book, and now you need something new to do. God, you wished today was a more eventful day.")
  time.sleep(3)
  decisionbook = input("\nWhat should you do next? Press N to nap, and T to drink tea: ")
  
  while decisionbook != "N" and decisionbook != "T":
    print("Not a valid answer.")
    decisionbook = input("\nPress N to nap and T to drink tea: ")
  if decisionbook == "N": 
    choicenap()
  elif decisionbook == "T": 
    choicetea()

def choicenap(): 
  os.system('clear')
  print("That book did make you feel a little drowsy. So, a nap really is the best course of action! You go back into your bedroom, climbing into your bed.")
  time.sleep(3)
  print("\nYou pull the blankets over, and close your eyes. The world fades to black.")
  time.sleep(5)
  endofworld()

def choicetea():
  os.system('clear')
  print("You move to make some tea, for yourself. You break out your favorite earl tea, and once you're done, you sit back down at your table.")
  time.sleep(3.5)
  print("\nYou drink it slowly, staring out the window as you do so. It feels like hours pass, as you sit their in silence, barely moving, barely thinking.")
  time.sleep(6)
  endofworld()

def choiceturnontv(): 
  os.system('clear')
  print("You turn on your TV. Automatically, you see bright, blaring letters, flashing across the screen: THE WORLD PANICS - IS EVERYTHING GOING TO END TODAY?")
  time.sleep(3)
  decisionturnontv = input("\nPress P to panic and call your friend and T to turn off the TV and have some tea: ")

  while decisionturnontv != "P" and decisionturnontv != "T":
    print("Not a valid answer.")
    decisionturnontv = input("\nPress P to panic and call your friend and T to turn off your TV and drink tea: ")
  if decisionturnontv == "P": 
    choice2callsomeone()
  elif decisionturnontv == "T": 
    choicetea()

#Option 2: Calling a friend about it to ask them
def choice2callsomeone(): 
  os.system('clear')
  print("It's the end of the world! All you can think of is that you need to call someone, right now.")
  time.sleep(3)
  decisionwhotocall = input("\nPress M to call your mother, and F to call your friend: ")
  
  while decisionwhotocall != "M" and decisionwhotocall != "F":
    print("Not a valid answer.")
    decisionwhotocall = input("Press M to call your mother, and F to call your friend: ")
  if decisionwhotocall == "M": 
    choicemom()
  elif decisionwhotocall == "F": 
    choicefriend()

def choicemom():
  os.system('clear')
  print("The first thought in your head, is of course to call your mother! You have to make sure she's okay! You dial her number quickly.")
  time.sleep(3)
  print("\nYour mother doesn't pick up. You try to call her again, but your mother isn't answering her phone.")
  time.sleep(2.75)
  decisionmom = input("\nWell, there goes that plan. What should you do? Press L to leave your house instead, and C to call your friend: ")

  while decisionmom != "L" and decisionmom != "C":
    print("Not a valid answer.")
    decisionmom = input("\nPress L to leave the house or C to call your friend: ")
  if decisionmom == "L": 
    choice2leavehouse()
  elif decisionmom == "C": 
    choicefriend()

def choicefriend():
  os.system('clear')
  print("In your panic, you choose to call your friend. Your friend is a reliable person— they always know what they're talking about, and so they're who your mind goes to, to find a way to stay alive.")
  time.sleep(3.5)
  print("\nYou and your friend have a quick conversation. At the end, your friend tells you: I've heard that there's some sort of ship leaving the Earth at 1pm. If you meet me on Main Street, by my apartment, maybe we can get there together!")
  time.sleep(4)
  print("\nYou check the time. It's 12pm. Do you even have time to get to Main Street?")
  time.sleep(1.5)
  decisionfriend = input("\nYou either try... or you don't. Press M to try to get to Main Street, or T to give up and just go home and have a cup of tea as the world ends: ")

  while decisionfriend != "M" and decisionfriend != "T":
    print("Not a valid answer.")
    decisionfriend = input("\nPress M to try to get to Main Street or T to go home: ")
  if decisionfriend == "M": 
    choice2leavehouse()
  elif decisionfriend == "T": 
    choicetea()

#Option 3: Leaving your house and lookin around/confused
def choice2leavehouse(): 
  os.system('clear')
  print("In your panic, you dash out of your apartment, not even stopping to properly close your door. You rush down your stairs, and run out onto the street.")
  time.sleep(4.5)
  print("\nThere's a hoard of people outside— chaos everywhere as cars flood the streets, people in utter dissarray.")
  time.sleep(3)
  print("\nEveryone seems like they're trying to get somewhere... but it doesn't seem like there's anywhere to go.")
  time.sleep(3)
  print("\nAbove you, in the normally bright, sunny sky, lays a crack— a jagged red cut burned into the sky, replacing the ordinary bright blue.")
  time.sleep(3.5)
  decisionhouse = input("\nPress M to try and meet up with your best friend, and K to just keep running: ")

  while decisionhouse != "M" and decisionhouse != "K": 
    print("Not a valid answer.")
    decisionhouse = input("\nPress M to try and meet up with your best friend, and K to just keep running: ")
  if decisionhouse == "M": 
    choicemeetfriend()
  elif decisionhouse == "K": 
    choicerun()

def choicemeetfriend(): 
  os.system('clear')
  print("Your best friend! You have to find them.")
  time.sleep(2)
  print("\nYou run a couple streets down, to the block where you know your friend should be. In the chaos— the rush of people, the honking cars, the cracked sky, you notice your friend.")
  time.sleep(3.5)
  print("\nThe two of you converse, and your friend fills you in on all the details, of how the two of you should escape together.")
  time.sleep(3.5)
  decisionmeetfriend = input("\nPress K to keep going: ")

  while decisionmeetfriend != "K": 
    print("Not a valid answer.")
    decisionmeetfriend = input("\nPress K to keep going: ")
  if decisionmeetfriend == "K": 
    os.system('clear')
    print("As you keep running, you and your friend out of breath, no ship in sight, it's clear. The two of you... aren't gonna make it.")
    time.sleep(3)
    print("\nWhether your friend's ship was real or not... it took too much time trying to get there.")
    time.sleep (2)
    choicebeforetheend()

def choicerun():
  os.system('clear')
  print("You have to keep going. There's no other options, you're desperate to find a way out.")
  time.sleep(1.5)
  print("\nYou just keep running, your legs carrying you, your brain racing. You need to find a way off the planet.")
  time.sleep(2.5)
  print("\nInformation keeps coming to you. You remember that there were rumors of ships leaving the planet... maybe you can get on one of those?")
  time.sleep(3)
  decisionrun = input("\nYou're breaths are slowly becoming heavier. You're losing stamina. Press K to keep going to find a ship or G to give up now: ")

  while decisionrun != "K" and decisionrun != "G": 
    print("Not a valid answer.")
    decisionrun = input("\nPress K to keep going or G to give up: ")
  if decisionrun == "K": 
    choicefindship()
  elif decisionrun == "G": 
    choicebeforetheend()

def choicefindship():
  os.system('clear')
  print("Breath's heaving, stamina low, you finally find a ship! It looks like there's a line, at the front, and there are some people boarding it.")
  time.sleep(3)
  print("\nThe ship is sleek, fancy... there's a logo on the side that you vaguely recognize. It's a high-tech company, but it's not the type that would just provide extra seats. For extra people.")
  time.sleep(3.5)
  decisionship = input("\nStill... you need to try and get on. Press S to try and find a way to stow away on the ship or L to get in line: ")

  while decisionship != "S" and decisionship != "L": 
    print("Not a valid answer.")
    decisionship = input("\nPress S to stow away, or L to get in line: ")
  if decisionship == "S": 
    choicestowaway()
  elif decisionship == "L": 
    choiceline()
  
def choiceline(): 
  os.system('clear')
  print("You decide to get in line. It's the honorable thing to do, after all. But the moment you step towards the line, a security guard comes up.")
  time.sleep(3)
  print("\nThey ask to see ID, and when it's clear that you have none, they step in front of you. Blocking you from the line, and shaking their head. There's no way for you to get on.")
  time.sleep(4)
  decisionline = input("\nIs this it? Is this the end? Press S to try and stowaway, or G to give up: ")

  while decisionline != "S" and decisionline != "G": 
    print ("Not a valid answer.")
    decisionline = input ("\nPress S to stow away or G to give up: ")
  if decisionline == "S": 
    choicestowaway()
  elif decisionline == "G": 
    choicebeforetheend()

def choicestowaway():
  os.system('clear')
  print("You've been going at this for too long to give up now. Whatever it takes, you need to get on this ship. You don't want to be here when the world ends.")
  time.sleep(3)
  print("\nYou circle the back of the ship, making sure to keep out of the way of any people or eyes you spot. Then, your eyes land on something major: a cargo door, looking like it leads to the cargo bay. Sure, there's no seatbelts, but if you can get in there...")
  time.sleep(4.5)
  decisionstowaway = input("\nYou think, if you try, that you can make your way onto the cargoship. But it is a risk. If you fail now, there's no other options. You'll get caught, and likely not find another way off the Earth. Press K to keep going, to try and make it on to the ship or G to give up: ")

  while decisionstowaway != "K" and decisionstowaway != "G": 
    print("Not a valid answer.")
    decisionstowaway = input("\nPress K to keep going or G to give up: ")
  if decisionstowaway == "K":
    choicesuccess()
  elif decisionstowaway == "G":
    choicebeforetheend()

def choicesuccess(): 
  os.system('clear')
  print("Just as you're about to make your way on ship... the cargo doors close, automatically. You jump as high as possible, run to get there, but the door closes before you can make it on.")
  time.sleep(4.25)
  print("\nYou've failed.")
  time.sleep(1.5)
  print("\nYou wish... that there was another option. But you tried your hardest and it wasn't enough.")
  time.sleep(5)
  choicebeforetheend()

def choicebeforetheend(): 
  os.system('clear')
  print("You're running out of breath. You can't keep this up. Even if there's a way off this world... can you even get to it in time?")
  time.sleep(3)
  print("\nYou wish you're memory was better. You had forgotten that today was the end of the world... somehow. Maybe... blissful ignorance? You have a lot of regrets.")
  time.sleep(3.5)
  print("\nYou hope that in the end, the life you lived was worth it.")
  time.sleep (4)
  endofworld()

#and it all ends like this. 
def endofworld():
  os.system('clear')
  print("No matter what you did, or didn't do, hear you are. Staring up into the sky— to the ruby red that had grown across the sky, striking like a pool of blood.")
  time.sleep(3.25)
  print("\nYou close your eyes. you don't want to look at it. You know it's the end, but you've decided. You don't want to see it.")
  time.sleep(3)
  print("\nWith your eyes closed, you surrender yourself to the end.")
  time.sleep(2)
  print("\nEverything fades to black.")
  time.sleep (4)
  os.system('clear')
  time.sleep(2)
  decisionfinal = input("Press P to play again, or E to let that be your end: ")

  while decisionfinal != "P" and decisionfinal != "E": 
    print("Not a valid answer.")
    decisionfinal = input("\nPress P to play again or E to let that be the end: ")
  if decisionfinal == "P": 
    start()
  elif decisionfinal == "E":
    os.system('clear')
    time.sleep(3)
    print("The End.")

#the run command
start()