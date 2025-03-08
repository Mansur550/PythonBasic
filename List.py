sub=["c","c++", "java","python","os","toc"]
print(sub)

# list Operation
#print
print(sub[0])
print(sub[2:])
print(sub[-1])


# Search from the list
print("c++" in sub)
print("c+++" in sub)

# Add item in list
print((sub+ ["swift",27,89,46]))
#print(sub*3) #print list items 3 times

#insert in list
sub.insert(4,"orange")
print(sub)
sub.append("Physics")
print(sub)
#remove
sub.remove("Physics")
print(sub)



#length of list
print(len(sub))

#sorting
sub.sort()
print(sub)
n=[1,39,8,3,3,83,93,92,94,84,847,44,829,928,474,7483,4,3,83,383,3939,93,4,4949,9]

n.reverse()
print(n)

n.sort()
print(n)

n.pop()#removes last number
print(n)

n2=n.copy()#copy list element
print(n2)
n.clear()#clear all element of list
print(n)

#Finding index of element
pos=n2.index(83)
print(pos)

#caounrt function
c=n2.count(93)
print(c)
print(n)

