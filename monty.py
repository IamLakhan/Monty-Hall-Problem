from random import choice as pick

p_of_goat, p_of_money, rounds = 0, 0, 100000 # large no of rounds for better probability

for x in range(rounds):
	choice = pick(('goat', 'money', 'goat')) # randomly chosing door with either money or goat
	if choice is 'money':
		switch = 'goat' # If you chose the door of money the other door has goat
		p_of_goat += 1
	else:
		switch = 'money' # if you chose the door with goat the other door has money
		p_of_money += 1

# Calculating probability in percentage	
m = int((p_of_money/rounds)*100)
g = int((p_of_goat/rounds)*100)

print('Probability based on event of switching:')
# Results
print(f'Probability of getting money: {m}%')
print(f'Probability of getting goat: {g}%')
