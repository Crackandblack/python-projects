# This program says hello and asks for your name

print('Hello world!')

print('what is your name?') # ask for for name
myName = input()
print('It is good to meet you, ' + myName)
print('The lenght of your name is:')
print(len(myName))

print('What is your age?') # ask for your age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + 'in a year.')