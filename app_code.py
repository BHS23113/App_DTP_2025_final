"""This program is a sql and python database, it stores data for different exercises and allows the user to print them out in different catagories"""


#imports the database
import sqlite3

#connects the sqlite3 to the python
connection = sqlite3.connect("movies.db")
cursor = connection.cursor()

#a loop so the code will fun untill the user wants to end it
while True:
    choice = input("\nPress \033[36mI\033[0m to show a list with all the workouts, \033[36mO\033[0m to list a specific muscle group, \033[36mP\033[0m to list workout by category or \033[31mE\033[0m to end the program\n")
    #making the input a capital 
    choice_upper = choice.upper()

    #if the user enters "P" it will run this code
    if choice_upper == "P":
        
        while True:
            category = input("\nEnter \033[36mF\033[0m for Push, \033[36mG\033[0m for Pull or \033[36mH\033[0m for Legs:\n")
            category_upper = category.upper()
            if category_upper == "F":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 1")
                #ends the second while loop while staaying in the first
                break

            elif category_upper == "G":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 2")
                break

            elif category_upper == "H":
                result = cursor.execute("SELECT * FROM workout WHERE set_id = 3")
                break
            #handles miss inputs
            else:
                print("\n\n\033[31mInvalid category.\033[0m Please enter \033[36mF\033[0m, \033[36mG\033[0m, or \033[36mH\033[0m.\n")

        workout = result.fetchall()

        #prints workouts according to their input
        print("")
        for exercises in workout:
            print(str(exercises[0]) + '. - ' + exercises[1])
        print()

        #gives the user a option to end the code or go back to the start
        start = input("\n\nPress \033[36mR\033[0m to return or \033[31mE\033[0m to end:\n").upper()
        if start == "E":
            break
        elif start == "R":
            continue
        else:
            print("\n\n\033[31mInvalid input returning to main menu.\033[0m\n")
            continue
    #prints all from workout
    elif choice_upper == "I":
        result = cursor.execute("SELECT * FROM workout")
        workout = result.fetchall()

        print("")
        for movie in workout:
            print(str(movie[0]) + '. - ' + movie[1])
        print()

    elif choice_upper == "O":
        #a loop is used to ask the question again if a miss input is entered 
        while True:
            muscle_group = input("\nEnter the muscle group to search:\n")
            muscle_group_upper = muscle_group.upper()
            if muscle_group_upper == "BACK":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 1")
                break

            elif muscle_group_upper == "BICEPS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 2")
                break

            elif muscle_group_upper == "CALVES":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 3")
                break

            elif muscle_group_upper == "CHEST":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 4")
                break

            elif muscle_group_upper == "DELTS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 5")
                break

            elif muscle_group_upper == "GLUTES":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 6")
                break

            elif muscle_group_upper == "GRIP":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 7")
                break

            elif muscle_group_upper == "HAMSTRINGS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 8")
                break

            elif muscle_group_upper == "LATS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 9")
                break

            elif muscle_group_upper == "QUADS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 10")
                break

            elif muscle_group_upper == "SHOULDERS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 11")
                break

            elif muscle_group_upper == "TRICEPS":
                result = cursor.execute("SELECT * FROM workout WHERE muscle_id = 12")
                break
            
            else:
                print("\n\n\033[31mInvalid target muscle.\033[0m Please enter a muscle group.\n")

        workout = result.fetchall()

        #prints workouts according to their input
        print("")
        for exercises in workout:
            print(str(exercises[0]) + '. - ' + exercises[1])
        print()
        
    #ends the code
    elif choice_upper == "E":
        break
    
    #handles miss inputs
    else:
        print("\n\n\033[31mInvalid choice.\033[0m Please enter \033[36mF\033[0m, \033[36mG\033[0m, \033[36mH\033[0m. or \033[31mE\033[0m.\n")
        continue

#ends the connection for a clean shut down
connection.close()
