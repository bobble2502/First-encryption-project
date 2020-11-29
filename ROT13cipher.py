import time

#create two lists to use as substitution cipher 

shifter = []
alphab = str('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Num = list(range(1,27))


for char in alphab:
	shifter.append(char)

#create two dicts to allow input word chars to be referenced as key to return value to create cyphertext

Key = dict(zip(alphab, Num))
Encrypt = dict(zip(Num, alphab))
print("Welcome to my ROT13 Cipher Project")

time.sleep(1.5)

#function to capture input word/phrase that will be encrypted. Checks to make sure word/phrase is only alpha chars, no special or numbers
def inputword():
	while True:
		global enterword
		global phrase
		global strphrase
		enterword = input("Enter phrase to encrypt: ")
		phrase = enterword.split()
		strphrase = "".join(phrase)
		
		if strphrase.isalpha() == True:
			print("Phrase accepted")
			break
		else:
			print("Enter letters only, no numbers or special characters")
inputword()

time.sleep(2)

#function to shift chars by 13 places to create ciphertext

def encryptionfunction():
	global ciphertext, keytext, encrypttext
	keytext = []
	encrypttext = []
	ciphertext = []
	for p in strphrase:
		p = p.upper()
		keytext.append(Key.get(p))

	for k in keytext:
		int(k)
		k += 13
		encrypttext.append(k)

	for e in encrypttext:
		if e > 26:
			e -= 26
		ciphertext.append(Encrypt.get(e))

	ciphertext = ''.join(ciphertext)
		
encryptionfunction()

#prints out function with added delays to add to user experience
print("Working...")

time.sleep(1)

print("Almost done...")

time.sleep(1)

print(F"Your encrypted message is: {ciphertext}.")

