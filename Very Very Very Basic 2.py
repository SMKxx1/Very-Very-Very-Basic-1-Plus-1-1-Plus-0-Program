def student1(eng_marks1, acc_marks1, ip_marks1):
    dic_std_name1 = {'eng':eng_marks1,'accounts':acc_marks1,'ip':ip_marks1}
    av1 = (eng_mark1 + ip_mark1 + acc_mark1) / 3
    return av1 #Return command is explained in line 43

def student2(eng_marks2, acc_marks2, ip_marks2):
    dic_std_name2 = {'eng':eng_marks2,'accounts':acc_marks2,'ip':ip_marks2}
    av2 = (eng_mark2 + ip_mark2 + acc_mark2) / 3
    return av2

def student3(eng_marks3, acc_marks3, ip_marks3):
    dic_std_name3 = {'eng':eng_marks3,'accounts':acc_marks3,'ip':ip_marks3}
    av3 = (eng_mark3 + ip_mark3 + acc_mark3) / 3
    return av3

print()
std_name1 = input("Enter the name of the student:")
eng_mark1 = int(input("Enter marks in english: "))
ip_mark1 = int(input("Enter marks in ip: "))
acc_mark1 = int(input("Enter marks in accounts: "))
print()

print()
std_name2 = input("Enter the name of the student:")
eng_mark2 = int(input("Enter marks in english: "))
ip_mark2 = int(input("Enter marks in ip: "))
acc_mark2 = int(input("Enter marks in accounts: "))
print()

print()
std_name3 = input("Enter the name of the student:")
eng_mark3 = int(input("Enter marks in english: "))
ip_mark3 = int(input("Enter marks in ip: "))
acc_mark3 = int(input("Enter marks in accounts: "))
print()

av1 = student1(eng_mark1,acc_mark1,ip_mark1)
av2 = student2(eng_mark2,acc_mark2,ip_mark2)
av3 = student3(eng_mark3,acc_mark3,ip_mark3)


'''
let me explain def function and return properly
for instence we have a program to find sum of two numbers

def sum(x,y):
    z = x + y
    return z
    
Now the function requires 2 variables (the x and y given in the parenthesis)
so lets create two variables

num1 = 5
num2 = 10

Finally lets run the function

the_sum_of_the_numbers = sum(num1,num2)

what happenes here is num1 and num2 replaces x and y.
also, the_sum_of_the_numbers will take the value of z because thats what we are returning or spitting out (probably returning is a better word)
'''


x = 0

while x < 3:
    average = [av1,av2,av3]
    avx = average[x]
    if avx >= 90:
        print("Average of",avx,"A grade")
    elif avx >= 70 and avx <= 89:
        print("Average =",avx,"B grade")
    elif avx >= 50 and avx <= 69:
        print("Average =",avx,"C grade")
    else:
        print("Average =",avx,"E grade")
    x += 1

min = max = mid = 0
if av1 < av2 and av1 < av3:
    if av2 < av3:
        min,mid,max = av1,av2,av3
    else:
        min,mid,max = av1,av3,av2
elif av2 < av1 and av2 < av3:
    if av1 < av3:
        min,mid,max = av2,av1,av3
    else:
        min,mid,max = av2,av3,av1
else:
    if av1 < av2:
        min,mid,max = av3,av1,av2
    else:
        min,mid,max = av3,av2,av1

print()
print("The topper is",max)
if max == av1:
    print(std_name1,"is the topper")
elif max == av2:
    print(std_name1)
