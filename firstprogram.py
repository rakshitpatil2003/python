# print("hello world")
# print("Rakshit Patil")

# print("hello "," how are you")

# name="rakshit"
# age=21
# price=10.10

# print("my name is : ",name)
# print("my age is : ",age)

# print(type(name))

# name1='rp'
# name2="rp"
# name3='''rp'''
# print(name1,name2,name3)

# old=False  #boolean value
# a=None #none data type ,abhi isme kuch bhi nahi hai

# a,b=2,3
# txt='@'
# print(a*txt*b)

# movie1=input("enter the 1st fav movie : ")
# movie2=input("enter the 2nd fav movie : ")
# movie3=input("enter the 3rd fav movie : ")

# list=[]
# list.append(movie1)
# list.append(movie2)
# list.append(movie3)

# print(list)


# def calc_fact(a):
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     return fact

# ans=calc_fact(10)
# print(ans)
# def evenodd(n):
#     if(n%2==0):
#         print("not a prime number")
#     else:
#         print("number is a odd number")    



# n=int(input("enter the number to be checked"))
# anser=evenodd(n)




# f=open("demo.txt","r")

# data=f.read()
# print(data)
# print(type(data))
# f.close()








class student:

    college_name="pallotti college"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("new student data is entered...")

s1=student("rakshit",50)
print(s1.name)
print(s1.marks)
print(s1.college_name)


s1=student("krutika",100)
print("name : ",s1.name)
print("marks : ",s1.marks)
print("college : ",s1.college_name)
print("rakshit")