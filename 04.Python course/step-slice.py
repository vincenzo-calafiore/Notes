parrot = "Norwegian Blue"

print(parrot[0:6:2]) # 0 to 5 (because the 6 is NOT INCLUDED) in steps of 2 =  N . r . e , Jumps 1
print(parrot[0:6:3]) # 0 to 5 in steps of 3 = N . . w  , jumps 2

number ="9,223,372,036,854,775,807"
print(number[1::4]) #start at 1 = , and ends at the end of the line stepping by 4 = . , . . . , . . . , . . . , [...]
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

