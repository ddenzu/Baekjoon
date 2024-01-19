a = ['c=','c-','dz=','d-','lj','nj','s=','z=']
d = ['a', 'b', 'c',
 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
b = input()
for i in a:
    if i in b:
        c = b.count(i)
        b = b.replace(i, '*')
        # print(b)

print(len(b))