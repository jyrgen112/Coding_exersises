fruitlist = ["apple", "banana", "cherry"]
print(fruitlist[0])
fruitlist.append("banana")
print(fruitlist)
print(fruitlist[-1])
#fruitlist(1) = (green)
print (fruitlist)
if "apple" in fruitlist:
    print ("apple, is on the list")
    
    print(len(fruitlist))
    fruitlist.pop(1)
    print (fruitlist)
    fruitlist.remove