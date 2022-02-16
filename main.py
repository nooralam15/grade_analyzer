#import libraries
import random
import sys


#Create a global variable
grades = []


#create an array that will display the grades and push 50 random grades
def createGrades():
    i = 0
    while i < 50:
        grades.append(random.randint(0,100))
        i += 1
createGrades()


#Initiliaze a function that will display all the grades
def displayGrades():
    for x in grades:
        print(x)


#Initliaze a function that will count and display total number of grades greater than 80
def honors():
    #create a variable to keep track of count
    count = 0
    #create a for loop
    for i in grades:
        if i > 80:
            count += 1
    print("There are " + str(count) + " grades that are honors")


#Intialize an array that will Determine and output the highest grade, lowest grade and average grade.
def stats():
    #set up variables 
    max_Grade = str(max(grades))
    min_Grade = str(min(grades))
    count = 0
    #loop through the array and find the sum of the array 
    for x in range(len(grades)):
        count += grades[x]
    #display the results
    print("Highest grade is " + max_Grade)
    print("Lowest grade is " + min_Grade)
    print("Average grade is " + str(count/len(grades)))


#intitialize a function that will display the menu
def menu():
    #initialize variable
    loop = True
    #create a while loop that will loop through the menu
    while loop:
        #print the the title of the menu
        print("Main Menu")
        userInp = input("Enter the number \n 1. Display All Grades \n 2. Randomize Grades \n 3. Stats \n 4. Count Honors \n 5. Exit\n")
        
        if userInp == "1":
            displayGrades()

        elif userInp == "2":
            createGrades()
            print("Grades added")

        elif userInp == "3":
            stats()

        elif userInp == "4":
            honors()

        elif userInp == "5":
            print("Program closed")
            sys.exit()

        else:
            print("Invalid Response")
menu()