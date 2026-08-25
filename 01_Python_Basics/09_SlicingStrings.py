word = "amazing"

result = word[0:3] #This gives the substring of the string from index 0 to 2
print(result) #This will print "ama"

result = word[3:7] #This gives the substring of the string from index 3 to 6
print(result) #This will print "zing"

result = word[1:6:2] #This gives the substring of the string from index 1 to 5 with a step of 2
print(result) #This will print "mzn"

result = word[:2] #This gives the substring of the string from index 0 to 1
print(result) #This will print "am"

result = word[2:] #This gives the substring of the string from index 2 to the end
print(result) #This will print "azing"

result = word[:] #This gives the substring of the string from index 0 to the end
print(result) #This will print "amazing"

result = word[-3:] #This gives the substring of the string from index -3 to the end

# the negative index starts from the end of the string, so -1 is the last character, -2 is the second last character and so on

print(result) #This will print "ing"

result = word[:-3] #This gives the substring of the string from index -7 to -4
print(result) #This will print "amaz"

result = word[-5:-2] #This gives the substring of the string from index -5 to -3
print(result) #This will print "azi"