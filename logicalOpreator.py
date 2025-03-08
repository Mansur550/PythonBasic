"""
Logical operator And, Or Not

"""
n1=1
n2=3
n3=7

if n1>n2 and n1>n3:
    print(n1)

if n2>n1 and n2>n3:
    print(n2)
else:
    print(n3)


#vowel_ a,e,io,u
ch=input()
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
    print("Vowel")
else:
    print("Consonant")