# program to find the highest number
def find_highest():

# input five numbers from the user
 num1 = int(input("Please input 1st number:"))
 num2 = int(input("Please input 2nd number:"))
 num3 = int(input("Please input 3rd number:"))         
 num4 = int(input("Please input 4th number:"))
 num5 = int(input("Please input 5th number:"))

#rank each number to determine the highest
 if num1 > num2:
    highest = num1 

 else:
    highest = num2

 if num3 > highest:
    highest = num3 

 if num4 > highest:
    highest = num4

 if num5 > highest:
    highest = num5
#print the highest number 

#call the function to run the program
find_highest()




