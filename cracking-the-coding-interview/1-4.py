# difficult implementation:

def shiftCharactersInList(a,index,howManyPlacesToShift):
	# find the last character thats not a space...
	# move move it
	i = len(a)-1
	while i > index:
		if a[i] != " ":
			a[i+howManyPlacesToShift] = a[i]
			a[i] = " "
		i = i -1
	return a




def replaceSpacesInCharArray(a):
	spacesInARow = 0
	for i in range(len(a)):
		if a[i] == " ":
			# we need to shift all the characters down... now it gets complicated!
			a = shiftCharactersInList(a,i,2)
			a[i] = "%"
			a[i+1] = "2"
			a[i+2] = "0"
			i = i + 2
		else:
			i = i+1
	return a










inputstring = ["M","r"," ","J","o","h","n"," ","S","m","i","t","h"," "," "," "," "]
print replaceSpacesInCharArray(inputstring)




#simple implementation
def replaceSpace(string):
	newString = ""
	for char in string:
		if char == " ":
			char = "%20"
		newString = newString + char
	return newString

