# Problem 2
n = 3
opt = 'y'
def errc(code):		# Function to display errors
	if code == 2:
		print("Invalid Position")
	elif code == 3:
		print("Position Already Occupied")
	elif code==4:
		print("You're supposed to enter an Odd number")
	elif code==5:
		print("You're supposed to enter an Even number")
	elif code==6:
		print("Err.. Number already exists")
	elif code==7:
		print("Enter the num in range (1-9)")

def isvalid(grid,pos,num, turn):	# Function to check if the input entered by player is valid or not
	pos = int(pos)
	num = int(num)
	turn = int(turn)
	if pos < 0 and pos > 9:		# Check for the position
		return 2
	if num<1 or num>9:		# Check for the number
		return 7
	x = int((pos-1) / 3)
	y = (pos-1) % 3
	if grid[x][y] != 0:		# If location is already occupied or not
		return 3
	if (num % 2 == 0 and turn == 1):	# If one enters a number which it is not supposed to
		return 4
	if (num % 2 == 1 and turn == 2):	# --do--
		return 5
	for i in range(3):			# If the entered number already exists
		for j in range(3):
			if grid[i][j] == num:
				return 6;
	return 1

def gridPrint(grid,pos,num,turn):		# Function to print and analyse the grid
	pos = int(pos)
	num = int(num)
	x = int((pos-1) / 3)
	y = (pos-1) % 3
	grid[x][y] = num
	count = 0
	# Printing the Grid
	print("____________")
	for i in range(3):
		for j in range(3):
			print(grid[i][j],end =' | ')
		if grid[i][j] != 0:
			count += 1
		print("\n____________")
	# Checking part
	Sumx =0
	Sumy =0
	err = 0
	for i in range(3):
		Sumx += grid[x][i]
		if grid[x][i] == 0:
			err = 1
			Sumx = 0
			err = 0
			break

	for i in range(3):
		Sumy += grid[i][y]
		if grid[i][y] == 0:
			err = 1
			Sumy = 0
			err = 0
			break
	if Sumx == 15 or Sumy == 15:
		return turn
	diagP = 0
	diagS = 0
	
	if x == y:	# Primary Diagnol
		for i in range(3):
			diagP += grid[i][i]
			if grid[i][i] ==  0:
				err = 1
				diagP = 0
				err = 0
				break

	if diagP == 15:
		return turn
	if x+y ==2:
		for i in range(3):
			diagS+= grid[i][2-i]
			if grid[i][2-i] == 0:
				err=1
				diagS=0
				break
	
	if diagS == 15:
		return turn
	if count == 9:
		return -1
	return 0
print("---\t Welcome to the Game! \t---")
while opt == 'y':
	turn = 1
	grid = [[0 for i in range(3)] for j in range(3) ]
	while 1:
		print("\nPlayer",turn,"'s turn\n")
		pos,num = input("Enter the position and number to be entered:").split()
		val = isvalid(grid,pos,num,turn)
		if val != 1:
			print("wrong input\n")
			errc(val)
			continue
		
		res = gridPrint(grid,pos,num,turn)
		if res == -1:
			print("It's a Draw\n")
			break
		elif res == turn:
			print("Player ",turn," wins\n")
			break
		if turn == 1:
			turn = 2
		else:
			turn = 1
	opt = input("Want to play again ? (y|n)")
	

