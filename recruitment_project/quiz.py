q1 = """ Is Python case sensitive when dealing with identifiers? 
a. Yes 
b. No
c. Machin dependent
d. None
"""
q2 = """ Which of the following is not a keyword? 
a. eval
b. assert
c. local
d. pass
"""
q3 = """ Which one of these is floor division? 
a. /
b. //
c. %
d. None
"""
q4 = """ What is the output of 3*1**3?
a. 27
b. 9
c. 3
d. 1
 """ 
q5 = """ "a" + "bc" = ?
a. a
b. bc
c. bca
d. abc
 """

questions = {q1:"a", q2:"a", q3:"b", q4:"c", q5:"d"}

name = input("Enter your name: ")
print("Welcome " + name + " to your quiz rounds")
print("All the best !!!")
score = 0

for i in questions:
    print("\n")
    print(i)        ## Question and their options 
    answer = input("Enter your answer: (a/b/c/d)")
    if answer == questions[i]:
        print("Correct answer !!! You got 1 point")
        score = score+1
    else:
        print("Wrong answer !!! lost 1 point")
        score = score-1

print("\n")
print("Final score is: ", score)

if score >= 3:
    print("\n")
    print("congratulations !!! You are selected for the next round ")    
else:
    print("\n")
    print("Sorry You have not cleared this round !!! Better luck next time")




