hiddenMes = raw_input("Enter a message to decrypt:\n>")



def by4(s):
    out = []
    while len(s):
        out.insert(0, s[-4:])
        s = s[:-4]
    return out

numList = by4(hiddenMes)






alphabet = [' ' ,'a', 'b', 'c', 
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
	x = x * 12
	x = x-21
	x = x / 34
	x = x + 62
	x = x - 504 
	x = x / 9
	x = x - 1
	numList2.append(x)

clearMesList = []
for x in numList2:
	y = 1
	
	#Checks to see if message character is equal to alphabet letter 
	while x != y:
		y = y + 1
		#If the character is not a letter, then it is represented by a 0
		if y > 46:
			y = 0
			break
	#Adds now converted character to numList 
	clearMesList.append(alphabet[y])


clearmessage = "".join(clearMesList)

print "Decrypted Message:\n" + clearmessage

	
