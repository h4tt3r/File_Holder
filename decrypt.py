hiddenMes = raw_input("Enter a message to decrypt:\n>")



def by5(s):
    out = []
    while len(s):
        out.insert(0, s[-5:])
        s = s[:-5]
    return out

numList = by4(hiddenMes)






alphabet = [' ', 'a', 'b', 'c', 
			'd', 'e', 'f', 
			'g', 'h', 'i', 
			'j', 'k', 'l', 
			'm','n', 'o',
			'p', 'q', 'r', 
			's', 't', 'u',
			'v', 'w', 'x', 
			'y', 'z', 'A', 
			'B', 'C', 'D', 
			'E', 'F', 'G', 
			'H', 'I', 'J', 
			'K', 'L', 'M', 
			'N', 'O', 'P', 
			'Q', 'R', 'S', 
			'T', 'U', 'V', 
			'W', 'X', 'Y', 
			'Z']
			
numList2 = []
y = 0
for x in numList:
	x = int(x)
	x = x + 743
	x = x - 23 
	x = x / 17
	x = x - 1000
	numList2.append(x)


clearMesList = []
for x in numList2:
	y = 1
	
	#Checks to see if message character is equal to alphabet letter 
	while x != y:
		y = y + 1
		#If the character is not a letter, then it is represented by a 0
		if y > 45:
			y = 0
			break
	#Adds now converted character to numList 
	clearMesList.append(alphabet[y])


clearmessage = "".join(clearMesList)

print "Decrypted Message:\n" + clearmessage
	

