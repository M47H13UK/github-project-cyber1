H = 'hELLO hHHeelEEoeloss'
hello = 'hello'.upper()
print(hello)


hello2 = 'HellOO'.lower()

print(hello2)
print(H.upper(), H.lower())
print(H.capitalize())
#.capitalize() formats the string so its like a scentece with the first letter capital. 

print(H.count('L'))
#counts the number of single capital L's
print(H.count('LL'))
#counts the number of dounble capital L's

#to count the total number of a ltter you can converet to upper or lower
print(H.upper().count('E'))
print(H.lower().count('h'))

#or directly count is a specified string in print.
print(str('Heeeeelleleleooooeoeoe woooowowwowssooowowrodlsssslslslslsworldsssss'.count('o'))*3)

y = 'yes'
n = 'no'
print(y*10)
print(y+n)
print(y,n)