from itertools import combinations
list = [6,3,-7,-4,-3,1]
print("possitive num are:")
for i in range (1,len(list)+1):
    for combo in combinations(list,i):
        if all (num>0 for num in combo):
            print (combo)
