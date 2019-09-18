# Program 1
bitStr = str(input("Enter the binary data to be transmitted\n"))
length = len(bitStr)
oneCount = 0;

#--------Parity Bit calculation---------
for i in range(length):
	if bitStr[i] == '1':
		oneCount += 1		#Increment '1' counter
	elif bitStr[i] != '0':
		print("Wrong input")	#Display error for non-binary input
		exit()			#Quit on error
# Appending corresponding parity bit
if oneCount % 2 == 0:
	bitStr = bitStr + '1'		#Appending parity bit
else:
	bitStr = bitStr + '0'
	
print("Parity Bt Data :",bitStr)

#------------ Bit Stuffing-------------
length = len(bitStr)
txData = ''
pat =str('010')				# Pattern to be identified
while 1:
	ind =  bitStr.find(pat)	 	# Find first occurrence of pattern
	if ind==-1:			# Break if no pattern found
		break		
	txData += bitStr[0:ind+3]	# Append the data upto pattern
	txData += '0'			# Stuff '0' bit
	bitStr = bitStr[ind+3:len(bitStr)]	# Update the original data
txData += bitStr			# Append the remaining data
txData += '0101'			# Ending flag
print("Transmitting Data :",txData)	
