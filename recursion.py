

import random

random.seed()

print(random.random())

randomNumbers = []

for i in range(20):

    randomNumbers.append(int(random.random()*50))

print (randomNumbers)



listONumbers = []

for i in range(2,27):
    listONumbers.append(i)

# print (listONumbers)



# print(listONumbers.pop())

# print(listONumbers)
sum1 = 0
for x in listONumbers:
    sum1 +=x





def findLargest(list):

    # if the list has more than one value
    if(len(list) > 1):

        # store value to test and shorten list by 1
        testValue = list.pop()

        # test if value is greater than greatest value so far
        if(testValue > list[0]):
            
            # store greatest value in index position 0
            list.insert(0,testValue) 


        print(list)
        print(len(list))

        return findLargest(list)

    else:

        return list[0]






def sum(list):

    # if list has one value left
   if(len(list) == 1): 

        # save last value and reduce list by 1
        s = list.pop()
    
        return s 
   
   else:
       
       # save last value and reduce list by 1
       s = list.pop() 

       #add value to next recursion 
       return s + sum(list)
   
# y = sum(listONumbers)

# print(y)

# print(sum1)


x = findLargest(randomNumbers)

print(x)