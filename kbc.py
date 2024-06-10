questions=[["Who dceveloped Python Programming language?",
            "a.Wick van Rossum b.Rasmus Lerdorf c.Guido van Rossum d.Niene"],
           ["Which keyword is used for function in Python language",
            "a.Function,b.def,c.Fun,d.Define"],
           ["Which of the following character is used to give single-line comment",
            "a.// b.# c.! d./*"],
           ["Which of the following statement is used to create an empty set in Python",
            "a.() b.[] c.{} d.set()"],
           ["To add a new element to a list we use which Python command?",
            "a.list1.addEnd(5) b.list1.addLst(5) c.list1.append(5) d.list1.add(5)"]
           ]
answers=['c','b','b','d','c']
print("Rules:\n")
print("Choose Correct Option[a-d] \n if 3-correct answers,you will win 5000 \n if give correct answer for all 5-questions then 10000 \n else zero(0)\n")
l=[]
amt=[1000,2000,5000,10000,20000]
homeTake=0
for index,val in enumerate(questions):
    cnt=0
    for i in range(len(val)):
        print(val[i])
    l.append(input())
    if answers[index]==l[index]:
        cnt=cnt+1
        print(f"Hurry, You won Rs.{amt[index]}")
        if index==4:
            homeTake=20000
        elif 2<=index<4:
            homeTake=5000
        else:
            homeTake=0
        print()
    else:
        print("Wrong Answer")
        break

print("Your total Winning amount is: Rs",homeTake)
