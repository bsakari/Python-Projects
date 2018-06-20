
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
print ("Good bye!\n\n\n")





for letter in 'Python':     # First Example
   print ('Current Letter :', letter)




print("\n\n\n")
fruits = ['banana', 'apple',  'mango']
for mimi in fruits:        # Second Example
   print ('Current fruit :', mimi)
print ("Good bye!\n\n\n")

#Nested Loop
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " is prime")
   i = i + 1

print ("Good bye!\n\n\n")







values = ["mom","dad","king"]
for x in values:
    if len(x)==3:
        print (x)