# Example Program for list insert & search Function

l = [10, 20 , 30 , 40 , 50]

l.append(30)
print(l)            # --->  [10, 20, 30, 40, 50, 30]

l.insert(1, 15)
print(l)            # --->  [10, 15, 20, 30, 40, 50, 30]

print(15 in l)      # --->  True

print(l.count(30))  # --->  2

print(l.index(30))  # --->  3

print(l.index(30, 4, 7))  # --->  6