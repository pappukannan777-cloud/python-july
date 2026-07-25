
import array as arr
fruit_count = arr.array('i',[3,5,2,4])
print("Fruit counts array:",fruit_count)
fruit_count.insert(0,1)
fruit_count.append(6)
print("Fruit counts after adding items:",fruit_count)
count_of_4=fruit_count.count(4)
print("number of times 4 appears:",count_of_4)
fruit_count.reverse()
print("reversed fruit counts array:",fruit_count)
