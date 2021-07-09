#"Python Crash Course" by Eric Matthes
# Chapter 7
#
#7-1
apples = int(input('How many apples would you like?_'))
if apples <10:
    print ('Feel free to help yourself to apple bags!\n')
else:
    print ('Please see attendant for assistance.\n')

#7-2
counting = int(input('What number would you like to begin counting at!?  \n'))
while counting <=100:
    print (counting)
    counting +=4

countdown =int(input('\nWhat number should we count down from!?'))
while countdown >=1:
    print (countdown)
    countdown -=4

#7-3
buying = '\nPlease provide your produce list. '
buying +='Enter "exit" to leave the produce program.\n'
response = ""
while response != 'exit':
    response = input (buying)
    print (f'You have entered: {response.title()}.')