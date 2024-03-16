# 1. The Calculator App

# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.

# while(True):
#     print("Welcome to The Calculator App")
#     num1 = int(input("Please enter a number: "))
#     op = input("Please enter an operation, (A)ddition, (S)ubtraction, (M)ultiplication, or (D)ivision: ").upper()
#     num2 = int(input("Please enter a number: "))

#     if op == 'A':
#         print(num1 + num2)
#     elif op == 'S':
#         print(num1 - num2)
#     elif op == 'M':
#         print(num1 * num2)
#     elif op == 'D':
#         if num2 == 0:
#             print("Error! We cannot divide by 0.")
#         else:
#             print(num1 / num2)
#     else:
#         print("Please enter a valid operator.")
    
#     inp = input("Enter (C)ontinue or (Q)uit: ").upper()
#     if inp == 'Q':
#         break
#     else:
#         pass

# 2. The Shopping List Maker

# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.
    
# item_list = []

# def addItem(item):
#     item_list.append(item)

# def removeItem(item):
#     if item in item_list:
#         item_list.remove(item)
#     else:
#         print("Item not found in the item list!")

# while(True):
#     inp = input("Enter (A)dd an item, (R)emove an item, or (P)rint item list: ").upper()
#     if(inp == 'A'):
#         item_to_add = input("Please enter an item to add: ")
#         addItem(item_to_add)
#     elif(inp == 'R'):
#         item_to_remove = input("Please enter an item to remove: ")
#         removeItem(item_to_remove)
#     elif(inp == 'P'):
#         for item in item_list:
#             print(item)
#     else:
#         print("Please enter a valid input.")

# 3. The Grade Analyzer

# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

# grades = [80, 93, 64, 91, 75]
# letters = [] * len(grades)

# def findAverageGrade(grades):
#     if(len(grades) > 0):
#         print(sum(grades) / len(grades))
#     else:
#         print("Please use a list of grades that is not empty!")

# def findLowestAndHighestGrade(grades):
#     print(min(grades), max(grades))

# def categorizeGrades(grades):
#     for i in range(0, len(grades)):
#         val = grades[i]
#         if val >= 90:
#             letters.append('A')
#         elif val >= 80:
#             letters.append('B')
#         elif val >= 70:
#             letters.append('C')
#         elif val >= 60:
#             letters.append('D')
#         else:
#             letters.append('F')
#     for letter in letters:
#         print(letter)

# findAverageGrade(grades)
# findLowestAndHighestGrade(grades)
# categorizeGrades(grades)

# 4. The Quiz Game

# Objective:
# The aim of this assignment is to create a quiz game that asks questions and checks answers.

# Task 1: Develop a list of questions and answers.
# Task 2: Write a function that quizzes the user and takes their answers.
# Task 3: Score the quiz and give the user feedback on their performance.

# questions = ["What is the capital of the United States?", "What is the capital of Colorado?", "What is the capital of Illinois?"]
# answers = ["Washington, D.C.", "Denver", "Springfield"]

# i = 0

# while(i < len(questions)):
#     print(questions[i])
#     inp = input("Please enter an answer: ")

#     if inp != answers[i]:
#         print("Incorrect answer! Please try again")
#     else:
#         i += 1

# 5. The Fitness Tracker

# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

# Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5

# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

activities = ["Running", "Walking", "Swimming", "Lifting"]
durations = [10, 20, 10, 30]

def logActivitiesAndDuration(activities, durations):
    i = 0
    while i < len(activities):
        print(activities[i], durations[i])
        i += 1

logActivitiesAndDuration(activities, durations)

def caloriesBurned(duration):
    return 3.5 * duration

for duration in durations:
    print(caloriesBurned(duration))

def logActivitiesAndDurationAndTotalCalories(activities, durations):
    i = 0
    while i < len(activities):
        print(activities[i], durations[i])
        i += 1
    print("Total calories burned is equal to:", 3.5 * sum(durations))

logActivitiesAndDurationAndTotalCalories(activities, durations)