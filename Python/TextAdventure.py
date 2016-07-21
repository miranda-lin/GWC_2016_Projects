start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
done = False
while user_input != "right" and user_input != "left":
	print("Please type 'left' or 'right'")
	user_input = input()
if user_input == "left":
	print('''You walk cautiously towards the left hallway. 
It's oddly quiet, except for a faint sound that you can't quiet make out. 
As you walk down the hallway, the sound grows steadily louder. "Thump. Thump. Thump."
You creep closer, curious about the cause of the sound.
You're nearing the end of the hallway, and it seems to be a dead end. 
You're about to turn back when all of a sudden the wall ahead of you is smashed open by an enormous club.
A troll staggers into view. Spotting you, it roars and starts lumbering towards where you are standing, frozen in fear.
			''')
	print("Do you want to fight or run? Type 'fight' to fight or 'run' to run.")
	user_input = input()
	while user_input != "fight" and user_input != "run":
		print("Please type 'run' or 'fight'")
		user_input = input()
	if user_input == "fight":
		print('''You charge at the troll, with nothing but your bare hands.
The troll snarls and raises its club. 
You dart around its legs, throwing punches and dodging the enormous feet.
CRASH! The troll brings its club down. 
You manage to evade the blow, watching the club crash down to where you were standing moments ago.
You feel your strength failing. Your blows are no more harmful to the troll than a fly to a human.
Your movements slow. Your reactions are much more delayed than before. 
You see one last chance to escape.
				''')
		print("Continue fighting or run? Type 'fight' to fight or 'run' to run.")
		user_input = input()
		while user_input != "fight" and user_input != "run":
			print("Please type 'run' or 'fight'")
			user_input = input()
		if user_input == "fight":
			print('''You make one last valiant effort to defeat the troll, but it just laughs and smashes you on the head as you collapse in exhaustion.
You drift off into oblivion...
					''')
		elif user_input == "run":
			print('''You seize the opportunity and sprint away from the troll. 
The troll laughs as it watches you run away.
You turn the corner at the end of the hallway and collapse from exhaustion, drifting off into sleep...
					''')
	elif user_input == "run":
		print('''The troll laughs as you run away like a baby.
When you've reached halfway across the hallway, you hear three thundering steps.
You turn around just in time to see the troll's club crashing down towards your head...
				''')

elif user_input == "right":
	print('''You walk down the right hallway. 
			You hear the sound of running water, and walk towards the sound. 
			The sound grows louder until you reach a rushing river. 
			You can see a village across the stream, maybe there will be someone there who knows where you are and what happened.
			''')
	print("Do you want to swim across? Type 'yes' to swim across or 'no' to stay.")
	user_input = input()
	while user_input != "yes" and user_input != "no":
		print("Please type 'yes' or 'no'")
		user_input = input()
	if user_input == "yes":
		print('''You plunge into the freezing water.
Teeth chattering, you struggle to move in the intense current
The river looks wider than it was before, and you question your decision to swim across.
But there's no turning back now, you're already sopping wet and have gone far enough that you can't get back.
Your limbs grow heavy as you try to fight the strong current.
Gasping for breath, you start to sink.
You try to continue swimming, but your body won't listen.
Your head sinks under the water and your vision blurs...''')
	elif user_input == "no":
		print('''You sit down next to the river and try to figure out what to do next.
The sun shining down warms your ody and the grass feels softer than feathers. 
You lie down on the grass and begin to drift off...''')


print('''Your eyes fly open. 
You're safe in your bed at home. 
The maze seems to have been a dream, the details fading away as you get up from bed.
You open your windows to let in some fresh air, when you notice a piece of paper on the windowsill.
You pick up the piece of paper and inspect it curiously. 
On the paper is a drawing of a maze...
		''')

