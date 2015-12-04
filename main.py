# Password Cracker
# By UP724145

import crypt

# The inputID and inputSalt are broken down to make it easier
# to change in the future
inputID = '6'
inputSalt = 'JOrEFPna'
cryptSalt = '$' + inputID + '$' + inputSalt
hashList = open("passwd", "r") #Change the file name for the hashes


# This method takes a line from the hash file and splits it into
# each component. These are then assigned to variables and returned
def splitHashList(line):
	singleHash = line.strip()
	singleHash = singleHash.replace(':', '$') # Replaces the end charecters to be stripped
	singleHash = singleHash.split('$') # Strips by the $ sign in the hash
	name = singleHash[0]
	id = singleHash[2]
	salt = singleHash[3]
	hash = singleHash[4]
	return name, id, salt, hash

# This method takes all the componants from the original hash and rebuilds them into
# a readable hash. It then iterates through each password in the file and hashes it
# using the same salt as the original. It then compares them together, if they are
# the same it prints the password and which user it relates to.
def compareHashes(name, id, salt, hash):
	reBuiltHash = '$' + id + '$' + salt + '$' + hash
	pwList = open("pwordList.txt", "r") # Change the file name for the hashes
	for line in pwList:
		word = line.strip()
		passwordHash = crypt.crypt(word, cryptSalt) #Hashes the word using original salt
		reBuiltPasswordHash = passwordHash
		if reBuiltPasswordHash == reBuiltHash:
			print ('Password cracked for ' + name + ' - Password is ' + word)
			break
	else:
		print ("No password found for " + name)
	pwList.close() # Closes the file after going through all the passwords

# This is the main function which loops through each hash and runs them though the
# two methods.
def main():
	for line in hashList:
		name, id, salt, hash = splitHashList(line)
		compareHashes(name, id, salt, hash)

if __name__ == "__main__":
	main()
