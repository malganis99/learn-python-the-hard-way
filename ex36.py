#text adventure made as an exercise for learn python the hard way


from sys import exit
from random import randrange

print "\tEnter commands without punctuation marks and in lower case letters."

print "\nYou have entered into a magic castle."
lives = 3


def counting_lives():
	global lives
	lives -= 1

	
def ama_room():
	question = raw_input("> ")
	
	sentence = question.split()
	#print sentence
	if 'complications' in sentence or 'problems' in sentence or 'problem' in sentence:
		print """\tMy prostate gets inflamed if I dont ejaculate enough.
\tI'm probably the only guy with a legit reason to orgasm at least
\tonce every day or two days. My prostate gets stimulation from both
\tcocks and creates a lot of seminal fluid. So when i cum it has to
\tbe squeezed every few days to get all the excess out. otherwise it
\tfeels bloated and painful."""
		ama_room()
	elif 'hard' in sentence:
		print """\tLeft one starts to get semi first,
\tthen stops at a certain point. Right one then gets 
\trock hard and if I'm horny enough the left one will
\tcontinue to stiffen up and get bigger. Once or twice, 
\twith a cock ring on, they've both been equally rock hard."""
		ama_room()
	elif 'pee' in sentence or 'peeing' in sentence:
		print """\tI generally avoid public bathrooms and if I do use one
\ti try to use the stall and not a wall urinal. There've been times where
\tI've had to use the urinal and because i have one muscle that controls 
\tmy piss, it lets the stream flow out both my dicks. so unless i pinch off 
\tone of them it comes out both and that doesnt feel good. So I have to take 
\tboth out to pee. Yeah Ive gotten stares and even had a few guys at various 
\ttimes go HOLY SHIT. """
		ama_room()
	elif 'leave' in sentence or 'exit' in sentence or 'open' in sentence:
		print "You don't want to be turned into a gay man so you go to another room."
		print "You see a big screen on the wall."
		print "You hear a deep voice coming from the screen."
		quiz_room()
	else:
		print "I don't understand your question."
		ama_room()
	
	
def groundhog_day():
	print "6 am \a\a\a"
	print """\n\tBabe, I got you babe
\tI got you babe."""

	next = raw_input("> ")
	
	lines = []
	line = raw_input()
	
	if 'groundhog day' in next:
		badger_room()
		
	while line != '':
		lines.append(line)
		line = raw_input()
		
	groundhog_day()
	
	
def quiz_room():
	print "\nWhat is the capital of Belize?"
	print "1. Baku, 2. Bangui, 3. Belmopan, 4. Banjul"

	next = raw_input("> ")
	
	if "3" in next:
		print "\nYour answer is correct."
		print "Doors open with a loud screech."
		print "'\nAhh, the great outdoors!'"
		print "'I've finally left this wicked castle.'"
		exit(0)
	elif "1" in next or "2" in next or "4" in next:
		print "\nNO! Wrong!"
		print "Guards appear and throw you into the dungeon."
		dungeon()
	else:
		print "\tInput the number from 1 to 4.\n"
		quiz_room()
		
	
def dungeon():
	next = raw_input("> ")
	
	mark_of_the_beast = 0
	
	while mark_of_the_beast != 666:
		mark_of_the_beast += 1
		print "\nBELMOPAN is the capital of Belize!!1!1!\tNow you will rot here until devil comes for your soul!\tMuahaha!", mark_of_the_beast

	print "Lightning strikes to the ground and in the cloud of smoke Devil himself appears."
	print "'I have come for your soul. If you give me your soul you may leave the dungeon'"
	print "'Otherwise you will be left here with rats.'"
	print "'Do you give me your soul?'"
	
	next = raw_input(">")
	
	if 'yes' in next:
		entrance()
	else:
		print "squeak, squeak, skreek..."
	
	
def open_the_door():
		print "\nYou turn the key inside the lock."
		print "Doors open and you step through to a long hall, until you reach next room.\n"
		print "I'm a man with two penises. AMA."
		ama_room()
	
	
def opening_chest():
	print "Pick the colour of the chest."
	
	next = raw_input(">")
	
	if "yellow" in next:
		print "\nAfrican snake jumps out and bites you."
		dead("You die slowly in pain.")
	elif "brown" in next:
		print "\nYou find a large iron key."
		print "This could prove useful."
		open_the_door()
	elif "red" in next:
		print "\nYou see a mushroom inside."
		print "It looks yummy. Let me taste it."
		print "You get so high you can't find way out."
		dead("Eventually you die from thirst.")
	elif "black" in next:
		groundhog_day()
	else:	
		"\tI don't know what you mean.\n"
		opening_chest()
		
		
def second_choice():
	next_action = raw_input("> ")
		
	if "go back" in next_action:
		entrance()
	elif "open the chest" in next_action:
		opening_chest()
	else:
		print "\tYou watch badgers dancing.\n"
		second_choice()
	
	
def badger_room():
	print "\nYou quickly look around and see four large wooden chests."
	print "They are yellow, red, brown, and black."
	print "Do you dare to open them?"
	
	next = raw_input(">")
	
	if "yes" in next:
		opening_chest()
	elif "no" in next:
		print "\nYou see the doors."
		print "You try to open them but they are locked."
		print "Hmm, key could be in one of the chests."
		print "What do you do? Go back or open the chest?"
		second_choice()
	else:
		print "\tI don't understand you.\n"
		badger_room()
				

def bear_room():
	print "\nA bear appears before you."
	print "GRRRRR"
	print "You shit your pants."
	print "\'I have to find a way out\'"
	print "1. You run back from where you came."
	print "2. You throw a beer at bear."
	
	next = raw_input("> ")

	if "1" in next:
		print "\'That was close.\'"
		print "You're back at hallway."
		entrance()
	elif "2" in next:
		chance = randrange(1,12)
		if chance < 5:
			print "\nBear gets really pissed and claws your face off."
			dead("Arrgh.")
		elif chance == 5 or chance == 6:
			print "\nBear catches the beer and takes a big gulp."
			print "You see a chance to escape and you jump through a hole in the wall."
			print "Slide takes you to another room."
			print "You see a big screen on the wall."
			print "You hear a deep voice coming from the screen."
			quiz_room()
		else:
			print "\nBear is temporarily blinded."
			print "You run back to hallway, relieved to escape from big bad bear."
			entrance()
	else:
		print "Not a valid choice"
		bear_room()
			
		
		
def entrance():
	print "There are doors on your left and right."
	print "Choose the doors."

	next = raw_input("> ")
	
	if "left" in next:
		bear_room()
	elif "right" in next:
		print "\nHere be badgers."
		print "They look very cute."
		print "They start dancing and singing."
		badger_room()
	else:
		print "\tYou walk around but nothing else is there.\n"
		entrance()
	

def dead(how):
	if lives != 0:
		counting_lives()	
		print "\nYou have %d lives left." % lives
		print "\nYou're back in a dark hallway."
		entrance()
	else:
		print how, "\tBetter luck next time."
		exit(0)
	
entrance()