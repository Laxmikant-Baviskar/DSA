# ============== First Solution =================

def average(l):
    sum = 0
    for x in l:
        sum = sum + x
    n = len(l)
    return sum/n

l = [10, 20 , 30 , 40]
print("The Average of given List is : " , average(l))


# output ---> The Average of given List is :  25.0

# ============== Second Solution =================

# using sum() Function directly

def average(l):
    return sum(l)/len(l)


l = [10, 20, 30, 40]

print(average(l))        # output --->  25.0
