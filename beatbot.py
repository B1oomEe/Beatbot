import random # random.randint(1, 100)
key = {
	'c': 0.1,
	'c#': 0.2,
	'd': 0.3,
	'd#': 0.4,
	'e': 0.5,
	'f': 0.6,
	'f#': 0.7,
	'g': 0.8,
	'g#': 0.9,
	'a': 1.0,
	'a#': 1.1,
	'b': 1.2
}
sclMin = [True, False, True, True, False, True, False, True, True, False, True, False]
sclMaj = [True, False, True, False, True, True, False, True, False, True, False, True]


musicalNotes = ['c','c#','d','d#','e','f','f#','g','g#','a','a#','b']

class Beatbot():

	def defineScale(key, fret): # define all scale notes by the key
		output = []
		usingScl = ''
		keyIndex = musicalNotes.index(key)

		# checking tonality (fret)
		if fret.lower() == 'min':
			usingScl = sclMin
		elif fret.lower() == 'maj':
			usingScl = sclMaj
		else:
			return f'This tonality -->{fret}<-- is not defined'

		for eachScl in usingScl:
			if eachScl == True: # check if note is in fret
				if keyIndex > 11:
					output.append(musicalNotes[keyIndex-12]) # add if notes in fret
				else:
					output.append(musicalNotes[keyIndex]) # add if notes in fret x2
			keyIndex+=1
		return output

	def generateMainKeys(scale):
		if scale[6] == False: # check if the scale is correct
			return f"Scale -->{scale}<-- is incorrect"
		numberMainNotes = random.randint(2, 4)
		random.shuffle(scale)
		output = []
		i = 0
		for note in scale:
			output.append(note)
			if i == numberMainNotes:
				return output
			i+=1
	def standartAccords(key, scale):
		return 0


mainScl = Beatbot.defineScale('d', 'min')
testNum = 0
while testNum < 10 :
	print(Beatbot.generateMainKeys(mainScl))
	testNum+=1
