# some General Purpose Functions in Python 

l = [10, 40, 20 ,50]

print(max(l))        # --->  50

print(min(l))        # --->  10

print(sum(l))        # --->  120

l.reverse()
print(l)             # --->  [50, 20, 40, 10]

l.sort()
print(l)             # --->  [10, 20, 40, 50]


# ===========================================================


# l = [10, "Boss" , 20 ,50]

# print(max(l))        # --->  Error 

# print(min(l))        # --->  Error

# print(sum(l))        # --->  Error

# l.reverse()
# print(l)             # --->  [50, 20, 'Boss', 10]

# l.sort()
# print(l)             # --->  Error


# ===========================================================

l = ["Boss" , "Toss" , "Khass" , "Fast"]


print(max(l))        # --->  Toss

print(min(l))        # --->  Boss

# print(sum(l))        # --->  Error

l.reverse()
print(l)             # --->  ['Fast', 'Khass', 'Toss', 'Boss']

l.sort()
print(l)             # --->  ['Boss', 'Fast', 'Khass', 'Toss']