dic = {}

def art():
    print('''

  ____  _             _            _         ____        _        
 / ___|| |_ _   _  __| | ___ _ __ | |_ ___  |  _ \  __ _| |_ __ _ 
 \___ \| __| | | |/ _` |/ _ \ '_ \| __/ __| | | | |/ _` | __/ _` |
  ___) | |_| |_| | (_| |  __/ | | | |_\__ \ | |_| | (_| | || (_| |
 |____/ \__|\__,_|\__,_|\___|_| |_|\__|___/ |____/ \__,_|\__\__,_|
                                                                  
 
''')

def add():
    std_name = input("Enter the name of the student: ")
    eng_marks = int(input("Enter the marks in English: "))
    ip_marks = int(input("Enter the marks in IP: "))
    acc_marks = int(input("Enter the marks in Accounts: "))
    dic[std_name] = {'English':eng_marks,'IP':ip_marks,'Accounts':acc_marks}
    print("The student data has been added")
    input()

def read():
    std_name = input("Enter the student name: ")
    if std_name in dic:
        print()
        print(std_name.capitalize(),"Scored")
        print(dic[std_name]['English'],"in English")
        print(dic[std_name]['IP'],"in IP")
        print(dic[std_name]['Accounts'],"in Accounts")
        print(std_name.capitalize(),"has an average marks of",(dic[std_name]['English']+dic[std_name]['IP']+dic[std_name]['Accounts'])/3)
        input()
    else:
        print("No student found...")
        input()

def update():
    std_name = input("Enter the student name: ")
    print()
    if std_name in dic:
        del dic[std_name]
        eng_marks = int(input("Enter the marks in English: "))
        ip_marks = int(input("Enter the marks in IP: "))
        acc_marks = int(input("Enter the marks in Accounts: "))
        dic[std_name] = {'English': eng_marks, 'IP': ip_marks, 'Accounts': acc_marks}
        print("Student profile successfully updated...")
        input()
    else:
        print("No student found...")
        input()

def dele():
    std_name = input("Enter the student name: ")
    del dic[std_name]
    print("Student data deleted...")
    input()
def main():
    while True:
        art()
        print('''
Select an option bellow:

1. Add a student's data
2. Read a student's data
3. Update a student's data
4. Remove a student's data

To stop the program type stop
''')
        opt = input("> ")
        if opt == '1':
            add()
        elif opt == '2':
            read()
        elif opt == '3':
            update()
        elif opt == '4':
            dele()
        elif opt == 'stop':
            break
        else:
            print("Invalid option")
            main()
main()