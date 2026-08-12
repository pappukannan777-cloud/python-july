from array import array

box1={"apple","banana","chips","apple","juice"}
box2={"banana","chips","cake","juice","chips"}

box1.add("banana")

common=box1.intersection(box2)

counts=array("i",[2,4,6,4,8])

counts.insert(0,10)
counts.append(12)

print("4 appears",counts.count(4),"times")

counts.reverse()

print("Snack Box 1:",box1)
print("Snack Box 2:",box2)
print("Common Snacks:",common)
print("Snack Counts:",counts)