print("hello "+input("what is ur name?")+"!")

name=input("what is your name?")
print("hello "+name)

n1=int(input())
n2=int(input())
print(n1*n2)

#finding length of string
numberofletters= len("prajna")
print(numberofletters)

Write a program that calculates and outputs the number of characters in any name. The automated tests will try out lots of different names as the input. Your code should work for any name. Your code should only output the number, no other text is needed
name=input()
print(len(name))
#or
print(len(input()))
