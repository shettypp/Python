#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#two_digit_num=print(input("enter 2 digit number"))...this give error because two_digit_num will be None because print() always returns None
two_digit_num=input("enter 2 digit number ")
num=str(two_digit_num)
a=int(num[0])
b=int(num[1])
print(a+b)
