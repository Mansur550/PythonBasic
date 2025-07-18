# # x= int(input("What is x?"))
# # y= int(input("What is y?"))
#
# # print(x+y)
#
# x= float(input("What is x?"))
# y= float(input("What is y?"))
#
# # z= round(x+y,)
# # print(f"{z:,}")
#
#
# z= x/y
# print(f"{z:.2f}")

def main():
    x= int(input("what is x? "))
    # y= int(input("What is y? "))

    print(x,"squared is", squared(x))


def squared(n):
    # return n * n
    # return n ** n
    return pow(n,2)

main()
