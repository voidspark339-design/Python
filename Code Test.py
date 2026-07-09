print('Programme starts')
print('hello world\n') 


'''
try:                         # try if the file exists, if false executes except and quit
   fhand = open("C:\\Users\\User\\Documents\\Python\\Python Test.txt", "r") 
   # fhand=handle if you print βγαζει μονο στοιχεια αρχειου
except :
   print('The file does not exist') 
   quit() 


for line in fhand :
     line=line.rstrip()
     print(line)            # print to file me for loop
print()
fhand.close()

fhand = open("C:/Users/User/Documents/Python/Python Test.txt", "r") 
print(fhand.read(), '\n')      # print to file ole me thn mia
fhand.close() 

fhand = open("C:/Users/User/Documents/Python/Python Test.txt", "r") 
print('number of chars in file', len(fhand.read()), '\n')     # lenght of chars in file
fhand.close() 

fhand = open("C:\\Users\\User\\Documents\\Python\\Python Test.txt", "a") 
newline ='\ngia na doume'
fhand.write(newline) 
fhand.close() 

count=0
for line in fhand :
    count = count +1
print ("number of lines =", count) 
fhnad.close() 

print("The searced line are the following:")
for line in fhand :
    if line.startswith('Kanw') :
       line=line.rstrip()
       print(line)
fhand.close()




for line in fhand :
    if not 'Kanw' in line:
        continue 
    line = line.rstrip()
    print(line) 
fhand.close() 
'''

                    # LISTS
newList=(['Mike', 'Ioanna', ['Shaolin', 'Whusu'], 'Giorgos'])     
print(newList[2])
fruit = 'Banana' # This is a string
print(fruit[0]) 
count=0  
for i in newList :  # iterate through the list
    count = count+1
print('itmes in list:', count) 

friends =['Tom', 'Nikos', 'George', 'Giannis Ixou']
for i in friends:
    print('How are you', i, '?')
print('End of programme')
print()