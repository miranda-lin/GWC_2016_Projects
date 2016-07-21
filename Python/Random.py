import random
import sys

def menu():
	adjs = ["Spicy", "Sweet", "Creamy", "Salty", "Savory", "BBQ", "Pesto", "Sour", "Peppery", "Aromatic"]
	styles = ["Sauteed", "Baked", "Seasoned", "Fried", "Grilled", "Roasted", "Caramelized", "Broiled", "Toasted", "Flambeed"]
	foods = ["Chicken", "Turkey", "Spinach", "Carrots", "Potatoes", "Steak", "Pork Chops", "Couscous", "Gnocchi", "Risotto"]

	def rand_item():
		return adjs[random.randint(0,9)] + " " + styles[random.randint(0,9)] + " " + foods[random.randint(0,9)]

	for i in range(10):
		print(rand_item())
	
def band():
	articles = ["The", "Three", "A", "Five", "Four", "Twelve"]
	adjs = ["Happy", "Funny", "Weird", "Running", "Loud", "Musical", "Hungry", "Exceptional", "Blue", "Purple"]
	items = ["Rocks", "Water Bottles", "Pens", "Rabbits", "Computers", "Dreams", "Oranges", "Blueberries"]
	def band_name():
		return articles[random.randint(0,5)] + " " + adjs[random.randint(0,9)] + " " + items[random.randint(0,7)]
	print(band_name())

def haiku():
	fives = ["With no leaves to blow", "They were whispering", "Yesterday morning", "It was much too late", "The world can decide", "It was a lost cause", "People will tell you", "They ran silently", "That was years ago", "Gusts of wind rising"]
	sevens = ["The wind is blowing softly", "The sand slipped through my fingers", "The enormous machines loom", "The orange lies on the desk", "Cold water drips on his head", "The dark forest was gloomy", "The vibrant red flower bloomed", "Dust covered the whole cottage", "The pungent smoke filled the air", "The blazing red fire burned on"]

	def a_haiku():
		return fives[random.randint(0,9)] + "\n" + sevens[random.randint(0,9)] + "\n" + fives[random.randint(0,9)]

	for i in range(3):
		print(a_haiku()+ "\n") 

def hangman():		
	words = ["political", "abruptly", "galaxy", "dwarves","papaya","karaoke","symphony","impromptu","rendezvous", "pneumonia", "oxygen","vaporize","jawbreaker","microwave","sequoia","exercise", "observation", "distance","experiment","weather", "balance","extraordinary", "composition", "vegetable", "property", "jazzy", "medicine", "conversation", "particularly","buzzing","hollow","surround", "discover", "environment", "molecule", "available", "forgotten", "consonant","announce", "fireplace", "mysterious","official","memory","melted","satellites", "occasionally", "elephant", "notebook", "rambunctious", "enthusiasm", "electronic", "activity", "character", "immutable", "submerge"]
	word = words[random.randint(0,len(words)-1)]
	answer = ""
	for i in range(len(word)): #prints out number of letters the hidden word has
		answer += "-"
	guesses = [] 
	done = False
	while done == False: #repeats until the player guesses the word
		repeat = True
		while repeat == True: #asks for another letter if already guessed
			letter = input("Guess a letter: ")
			j = 0
			repeat = False
			for i in range(len(guesses)): #checks wrong guess list if the user has already guessed the letter
				if guesses[j] == letter:
					repeat = True
				j+=1
			j = 0 
			for i in range(len(answer)):  #checks answers if the user has already guessed the letter
				if answer[j] == letter:
					repeat = True
				j+=1
				
				
		a = 0
		guessed = False	
		for i in range(len(word)): #checks if the guessed letter is in the word
			if word[a] == letter:
				answer = answer[0:a] + letter + answer[a+1:] #switches the '-' to show the correctly guessed letters
				guessed = True
			a+=1
		if guessed == False:
			guesses.append(letter) #adds the letter to wrong guess list if not in word
		if answer.find("-") == -1: #if all letters guessed, game over
			done = True
		print(answer)
		sys.stdout.write("Wrong guesses: ")
		c = 0
		for i in range(len(guesses)): #prints all the wrong guessed letters
			sys.stdout.write(guesses[c] + " ")
			c+=1
		print("\n")
	print("You Win!")



menu()
print("\n")
band()
print("\n")
haiku()
print("\n")
hangman()
