
# print("welcome to kbc")
# print("here is ur first question")
# print("what is the capital of india?")
# print("a-new delhi")
# print("b-pune")
# print("c-kolakatta")
# print("d-mumbai")

# question="A"
# question="B"
# question="C"
# question="D"
# q=input("pls choose your ans...")
# if q=="A":
#     print("u r right")
# elif q=="B":
#     print("u r wrong")
# elif q=="C":
#     print("u r wrong")
# elif q=="D":
#     print("u r wrong")
# else:
#     print("enter the valid option")

# print("here is ur second question")
# print("what is the capital of maharashtra?")
# print("a-nashik")
# print("b-delhi")
# print("c-mumbai")
# print("d-pune")
# q=input("pls chose ur ans...")
# if q=="A":
#     print("wrong")
# elif q=="B":
#     print("wrong")
# elif q=="C":
#     print("right")
# elif q=="D":
#     print("wrong")
# else:
# #     print("enter the valid option")



question_list = [ "1.How many continents are there?",           
    "2.What is the capital of India?" ,          
    "3.NG mei kaun se course padhaya jaata hai?" 
]
life_line=[5050]
opt1=["four","bhopal","software"]
opt2=["nine","chennai","councling"]
opt3=["seven","chandigrah","upsc"]
opt4=["eight","delhi","mpsc"]
opt6=["seven","bhopal","software"]
opt7=["four","delhi","upsc"]
ans = [1,2,1]
solution=[3,4,1]
i=0                                                                                                                             
c=0
while(i<len(question_list)):
    print("welcome to kaun banega crorepati")
    print(question_list[i])
    print(1,opt1[i])
    print(2,opt2[i])
    print(3,opt3[i])
    print(4,opt4[i])
    print(5, life_line[0])
    user=int(input("enter any num"))
    c=c+1
    if(solution[i]==user):
           print("congrats your answer is right")
    elif(user==5050):
        if c==0:
            print(1,opt6[i])
            print(2,opt7[i])
            user1=int(input("enter any num"))
            if(user1== ans[i]):
                print("Your answer is correct")
            else:
                print("your answer is wrong")
                bre
                print("sorry your answer is wrong")
            break
    i=i+1

# name = ["Savitri", "Phule", "26"]
# print(name[0]+name[1]+name[2])

# a=[2,3,4,5,6]
# print([a[4],a[0],a[3],a[1],a[2]])

# list1=[6,23,3,2,0,9,8,75]                
# print(list1[1:8:2])

