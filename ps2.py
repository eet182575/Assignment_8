# Problem 2
n = 3
opt = 'y'

def isvalid(grid,pos,num, turn):
	pos = int(pos)
	num = int(num)
	turn = int(turn)
	if pos < 0 and pos > 9:
		return 0
	x = int((pos-1) / 3)
	y = (pos-1) % 3
	if grid[x][y] != 0:
		return 0
	if (num % 2 == 0 and turn == 1) or (num % 2 == 1 and turn == 2):
		return 0
	return 1
def gridPrint(grid,pos,num,turn):
	pos = int(pos)
	num = int(num)
	x = int((pos-1) / 3)
	y = (pos-1) % 3
	print("X:",x, "Y:",y)
	print("XY: ",grid[x][y])
	grid[x][y] = num
	count = 0
	# Printing the Grid
	for i in range(3):
		#print(" _ \t_ \t_\n|")
		for j in range(3):
			print(grid[i][j]," ")
			if grid[i][j] != 0:
				count += 1
		print("\n")
	# Checking part
	Sumx =0
	Sumy =0
	err = 0
	for i in range(3):
		Sumx += grid[x][i]
		if grid[x][i] == 0:
			err = 1
			break
	if err==1:
		Sumx = 0
	err = 0
	for i in range(3):
		Sumy += grid[i][y]
		if grid[i][y] == 0:
			err = 1
			break
	if err==1:
		Sumy = 0
	
	if Sumx == 15 or Sumy == 15
		return turn
	diagP = 0
	diagS = 0
	err = 0
	if x == y:	# Primary Diagnol
		for i in range(3):
			diagP += grid[i][i]
			if grid[i][i] ==  0:
				err = 1
				break
	if err==1:
		diagP = 0
	err = 0
	if diagP == 15:
		return turn
 	if x + y == 2:	# Secondary Diagnol
		for i in range(3):
			diagS += grid[i][2-i]
			if grid[i][2-i] ==  0:
				err = 1
				break
	if err==1:
		diagS = 0
	
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
		print("Player",turn,"'s turn\n")
		pos,num = input("Enter the position and number to be entered:").split()
		val = isvalid(grid,pos,num,turn)
		if val == 0:
			print("wrong input\n")
			continue
		
		res = gridPrint(grid,pos,num)
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
	

