# Write a python code to accept a string and count the number of vowels and consonants.

#taking the input string
inp = input('Enter the string: ')

#initializing counters for vowels and consonants
v=0
c=0

#running a for loop to check all the characters of the input string
for i in inp:
  #checking if the character is a vowel, then increasing v by 1
  if i.lower() in ['a', 'e', 'i', 'o', 'u']:
    v=v+1
  #checking if the charcter is a space, then pass and do nothing
  elif i == ' ':
    pass
  #checking if the character is a consonant, then increasing c by 1
  elif i.isalpha():
      c = c + 1

#print the values of v and c
print('The number of vowels is', v)
print('The number of components is ', c)
