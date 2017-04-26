import random

f = open("words.txt","r")
lines=f.readlines()

dramatis_personae = [
	('man','woman'),
	('buil','phil'),
	('man','dog')
]

Apers,Bpers = random.choice(dramatis_personae)

AWords = []

for i in lines:
	if i.find(Apers)!=-1 and i.find(Bpers)==-1:
		AWords.append(i)
word = random.choice(AWords)
Bword = word.replace(Apers,Bpers).strip()

print Apers+": What shall we call this?"
print Bpers+": How about "+Bword
print Apers+": I have a better idea.."