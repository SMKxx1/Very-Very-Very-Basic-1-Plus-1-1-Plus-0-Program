dic = {} #This is creating an empty dictionary where the students data will be added
#The data will be stored as {student1 : { subject1 : subject1 marks, subject2 : subject2 marks, Grade: grade}, student2:{...}}

def art():
    print('''
  ____  _             _            _         ____        _        
 / ___|| |_ _   _  __| | ___ _ __ | |_ ___  |  _ \  __ _| |_ __ _ 
 \___ \| __| | | |/ _` |/ _ \ '_ \| __/ __| | | | |/ _` | __/ _` |
  ___) | |_| |_| | (_| |  __/ | | | |_\__ \ | |_| | (_| | || (_| |
 |____/ \__|\__,_|\__,_|\___|_| |_|\__|___/ |____/ \__,_|\__\__,_|''')

#Here i am making a function to assign a grade according to the average marks
#the variable x will be the average
def grade(x):
    if x >= 90:
        g = 'A'
    elif x >= 70:
        g = 'B'
    elif x >= 50:
        g = 'C'
    elif x >= 30:
        g = 'D'
    else:
        g = 'E'
    return g

#Here i am gonna make a function to add the students data
def add():
    std_name = input("Enter the name of the student: ") #this is the students name
    if std_name not in dic: #to check if the students data is already existing or not
        eng_marks = int(input("Enter the marks in English: ")) #marks in english
        ip_marks = int(input("Enter the marks in IP: ")) #marks in ip
        acc_marks = int(input("Enter the marks in Accounts: ")) #marks in accounts
        avg = (eng_marks + ip_marks + acc_marks)/3 #this is to find the average
        grd = grade(avg) #this will take the average and assign it a grade according to the grade function done previously
        # i am not creating a new dictionary.I am just adding the values to the empty dictionary that i have created before
        dic[std_name] = {'English':eng_marks,'IP':ip_marks,'Accounts':acc_marks,'Grade':grd}
        print("The student data has been added")
        input() #This input command serves no purpose in creating a variable but
        #but it is here just to stop the program from going any further unless the user commands it to
    else: #if the students data is already existing then it does the following
        print("Student data already existing...")
        input()

#this is to lay down the students information in an clean manner
def read():
    std_name = input("Enter the student name: ") #you enter the students name here
    if std_name in dic: #this if statement is to check is the student data is in the dictionary
        print()
        print(std_name.capitalize(),"Scored") # .capitalize is just capitalize the first letter of the name (to make it more presentable)
        print(dic[std_name]['English'],"in English") # finds the marks in english
        print(dic[std_name]['IP'],"in IP") # finds the marks in IP
        print(dic[std_name]['Accounts'],"in Accounts") # finds the marks in Accounts
        # next two lines is for presentation purpose only
        print(std_name.capitalize(),"has an average marks of",(dic[std_name]['English']+dic[std_name]['IP']+dic[std_name]['Accounts'])/3)
        print("The grade is",dic[std_name]['Grade'])
        input() #explained before
    else:
        print("No student found...") #if the students data is not found it prints this
        input()

#this is a function to make changes to pre-existing data
def update():
    std_name = input("Enter the student name: ") #enter the name of the student to find the data to be edited
    print()
    if std_name in dic: #if the students data is found
        del dic[std_name] #deletes the old data
        #next lines are identical to lines in the add() function
        eng_marks = int(input("Enter the marks in English: ")) #marks in english
        ip_marks = int(input("Enter the marks in IP: ")) #marks in IP
        acc_marks = int(input("Enter the marks in Accounts: ")) #marks in Accounts
        avg = (eng_marks + ip_marks + acc_marks)/3 #average marks
        grd = grade(avg) #grade assigned according to the grade function
        dic[std_name] = {'English':eng_marks,'IP':ip_marks,'Accounts':acc_marks,'Grade':grd} #adds the data into the dictionary
        print("Student profile successfully updated...") #PRESENTATION PURPOSE ONLY
        input()
    else:
        print("No student found...") #prints it only if the data is not found
        input()

#This function is to delete the pre-existing student data
def dele():
    std_name = input("Enter the student name: ") #name of the student to delete the data
    if std_name in dic:
        del dic[std_name] #del command deletes the data
        print("Student data deleted...") #PRESENTATION PURPOSE ONLY
        input()
    else:
        print("No such user...")
        input()

#This is the main code that will take the input from the user and execute the previous functions accordingly
def main():
    while True: #While True: is used to create an infinite loop that can only be stopped by using break statement or by keyboard interrupt (ctrl + c)
        art() #Prints the VERY VERY VERY IMPORTANT ART created before
        print('''
Select an option bellow:

1. Add a student's data
2. Read a student's data
3. Update a student's data
4. Remove a student's data

To stop the program type stop 
''')
        opt = input("> ")
        if opt == '1': #The number is given in quotes ('1') because the input statement does not have int in it
            add()
        elif opt == '2':
            read()
        elif opt == '3':
            update()
        elif opt == '4':
            dele()

        #If the user types stop or any of the statements (there are multiple just to create room for the user to breath)
        #it will initiate the break statement and stop the infinite loop
        elif opt == 'stop' or opt == 's' or opt == 'stop ':
            break
        else:
            print("Invalid option")
            input() #Explained before
            main() #if the option is invalid it repeats the program
main()

#If you have any doubts, please ask me and
#Feel free to check out my repository for the things i have created and the IP project i am working on (Password-storing-and-cracking)
#Just for the record. I am not a nerd...