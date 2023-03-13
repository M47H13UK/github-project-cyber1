#==  !=   <=   >=   < > 
x='hello'
y='hello'
z='hEllo'
print(x==y)
print(x!=y)
print(x==z)

#we can compare characters, its basedon the ascii code, you can check for the ordinal value of the character using ord()

one='a'
two='b'
three='c'
four='z'
five='Z'
six='A'

print(ord('a'))
print(ord(one))
print(ord(three))
print(ord(four))
print('-----')
print(ord(five))
print(ord(six))

print('a'>'Z')
print('A'>'Z')
print('-----')

#if you put multiple characters then it will compare one by one
print('ab'>'aa')
print('ab'>'abd')
print('ab'>'ac')
print('ab'>'ba')
print('ab'<'ba')
#so compares the first character with the first character then if they are identical moves on the next chracted unitl one is either greater of less than the other.






