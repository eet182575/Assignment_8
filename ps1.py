# Program 1
bitStr = str(input("Enter the binary data to be transmitted\n"))
length = len(bitStr)
oneCount = 0;

#--------Parity Bit calculation---------
for i in range(length):
	if bitStr[i] == '1':
		oneCount += 1
	elif bitStr[i] != '0':
		print("Wrong input")
		exit()
# Appending corresponding parity bit
if oneCount % 2 == 0:
	bitStr = bitStr + '1'
else:
	bitStr = bitStr + '0'
	
print("Parity Bt Data :",bitStr)

#------------ Bit Stuffing-------------
length = len(bitStr)
txData = ''
temp = ''
pat =str('010')
done =0
while 1:
	ind =  bitStr.find(pat)	 
	if ind==-1:
		break
	txData += bitStr[0:ind+3]
	txData += '0'
	bitStr = bitStr[ind+3:len(bitStr)]
txData += bitStr
txData += '0101'
print("Transmitting Data :",txData)
